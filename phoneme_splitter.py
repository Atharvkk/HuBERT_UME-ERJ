import os
import soundfile as sf
from textgrids import TextGrid

SAMPLE_RATE = 16000
IGNORE_PHONES = {"sil", "sp", ""}

BASE_DIR = r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize"
OUTPUT_DIR = r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize_Slices"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for university in os.listdir(BASE_DIR):
    uni_path = os.path.join(BASE_DIR, university)
    if not os.path.isdir(uni_path):
        continue

    for gender in ["MALE", "FEMALE"]:
        wav_dir = os.path.join(uni_path, gender, "WAV")
        tg_dir = os.path.join(uni_path, gender, "textgrid")

        if not os.path.exists(wav_dir) or not os.path.exists(tg_dir):
            continue

        out_dir = os.path.join(OUTPUT_DIR, university, gender)
        os.makedirs(out_dir, exist_ok=True)

        for tg_file in os.listdir(tg_dir):
            if not tg_file.endswith(".TextGrid"):
                continue

            utt_id = tg_file.replace(".TextGrid", "")
            wav_path = os.path.join(wav_dir, utt_id + ".wav")
            tg_path = os.path.join(tg_dir, tg_file)

            if not os.path.exists(wav_path):
                continue

            audio, sr = sf.read(wav_path)
            if sr != SAMPLE_RATE:
                raise RuntimeError(f"{utt_id}: expected 16kHz, got {sr}")

            tg = TextGrid(tg_path)
            phone_tier = tg["phones"]

            for idx, interval in enumerate(phone_tier):
                phone = interval.text.strip()
                if phone in IGNORE_PHONES:
                    continue

                start = int(interval.xmin * SAMPLE_RATE)
                end = int(interval.xmax * SAMPLE_RATE)
                if end <= start:
                    continue

                slice_audio = audio[start:end]

                out_name = f"{utt_id}_{idx}_{phone}.wav"
                out_path = os.path.join(out_dir, out_name)

                sf.write(out_path, slice_audio, SAMPLE_RATE)
