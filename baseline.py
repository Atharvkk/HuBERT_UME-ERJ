import os
import glob
import torch
import torchaudio
import textgrid
import numpy as np
import pickle
from transformers import Wav2Vec2FeatureExtractor, HubertModel
from tqdm import tqdm
from collections import defaultdict

MODEL_NAME = "facebook/hubert-base-ls960"
LAYER_ID = 9
SAMPLE_RATE = 16000

DATA_MAP = {
    "JapaneseOverall": {
        "wav": r"Z:\FluentifyAI\CodeBase\Phoneme_Data\ALL\ALL\WAV",
        "tg": r"Z:\FluentifyAI\CodeBase\Phoneme_Data\ALL\ALL\textgrid",
        "output": r"Z:\FluentifyAI\CodeBase\Final_Data\Japanese_composite.pkl"
    },
    "AmericanOverall": {
        "wav": r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize\AE\ALL\WAV",
        "tg": r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize\AE\ALL\textgrid",
        "output": r"Z:\FluentifyAI\CodeBase\Final_Data\American_composite.pkl"
    }
}

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.backends.cudnn.benchmark = True

def load_model():
    processor = Wav2Vec2FeatureExtractor.from_pretrained(MODEL_NAME)
    model = HubertModel.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if DEVICE.type == "cuda" else torch.float16
    )
    model.to(DEVICE)
    model.eval()
    return processor, model

def get_hubert_features(wav_path, processor, model):
    speech, sr = torchaudio.load(wav_path)
    if sr != SAMPLE_RATE:
        speech = torchaudio.functional.resample(speech, sr, SAMPLE_RATE)
    
    speech = speech.mean(dim=0, keepdim=True)
    inputs = processor(speech.squeeze(0), sampling_rate=SAMPLE_RATE, return_tensors="pt").input_values.to(DEVICE)
    
    if DEVICE.type == "cuda":
        inputs = inputs.half()

    with torch.inference_mode():
        outputs = model(inputs, output_hidden_states=True)
    return outputs.hidden_states[LAYER_ID][0].cpu().numpy()

def process_gender_corpus(wav_dir, tg_dir, processor, model):
    phoneme_pool = defaultdict(lambda: defaultdict(list))
    duration_pool = defaultdict(list)
    
    wav_files = glob.glob(os.path.join(wav_dir, "*.wav"))
    tg_files = glob.glob(os.path.join(tg_dir, "*.TextGrid"))
    tg_map = {os.path.basename(f).replace(".TextGrid",""): f for f in tg_files}

    for wav_file in tqdm(wav_files, desc="Processing Audio"):
        filename = os.path.basename(wav_file).replace(".wav", "")
        if filename not in tg_map: continue

        parts = filename.split("_")
        if len(parts) < 4:
            speaker_key = parts[-1] 
        else:
            speaker_key = f"{parts[2]}_{parts[3]}" 

        embeddings = get_hubert_features(wav_file, processor, model)
        total_frames = embeddings.shape[0]

        tg = textgrid.TextGrid.fromFile(tg_map[filename])
        try:
            phone_tier = tg.getFirst("phones")
        except ValueError:
            phone_tier = tg[1]

        duration = tg.maxTime
        frame_rate = total_frames / duration

        for interval in phone_tier:
            phone = interval.mark.strip()
            if phone in {"", "sil", "sp"}: continue

            start = int(interval.minTime * frame_rate)
            end = int(interval.maxTime * frame_rate)
            
            if end > start:
                vec = embeddings[start:end].mean(axis=0)
                phoneme_pool[phone][speaker_key].append(vec)
                duration_pool[phone].append(interval.maxTime - interval.minTime)

    return phoneme_pool, duration_pool

def calculate_statistics(phoneme_pool, duration_pool):
    baseline = {}
    for phone, speakers in phoneme_pool.items():
        all_vecs = [v for s_vecs in speakers.values() for v in s_vecs]
        X = np.stack(all_vecs)
        
        speaker_means = np.stack([np.mean(v, axis=0) for v in speakers.values()])
        
        baseline[phone] = {
            "mu_global": X.mean(axis=0),
            "mu_speaker_norm": speaker_means.mean(axis=0),
            "std_global": X.std(axis=0),
            "inter_speaker_std": speaker_means.std(axis=0),
            "dur_mu": np.mean(duration_pool[phone]),
            "dur_std": np.std(duration_pool[phone]),
            "token_count": X.shape[0],
            "speaker_count": len(speakers)
        }
    return baseline

def main():
    processor, model = load_model()

    for gender, paths in DATA_MAP.items():
        print(f"\n{'='*40}\nINITIATING {gender.upper()} PIPELINE\n{'='*40}")
        
        pool, durations = process_gender_corpus(paths["wav"], paths["tg"], processor, model)
        stats = calculate_statistics(pool, durations)

        os.makedirs(os.path.dirname(paths["output"]), exist_ok=True)
        with open(paths["output"], "wb") as f:
            pickle.dump(stats, f)
        
        print(f"SUCCESS: {gender.upper()} stats saved.")

if __name__ == "__main__":
    main()