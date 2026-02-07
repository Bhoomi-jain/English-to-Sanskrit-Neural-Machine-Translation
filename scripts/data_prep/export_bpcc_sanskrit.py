from datasets import load_dataset
from tqdm import tqdm
from pathlib import Path

# Output directory
out_dir = Path("data/raw/bpcc")
out_dir.mkdir(parents=True, exist_ok=True)

ds = load_dataset(
    "ai4bharat/BPCC",
    "bpcc-seed-latest",
    split="san_Deva"
)

with open(out_dir / "train.en", "w", encoding="utf-8") as fe, \
     open(out_dir / "train.sa", "w", encoding="utf-8") as fs:

    for row in tqdm(ds):
        en = row["src"].strip()
        sa = row["tgt"].strip()

        if len(en.split()) >= 3 and len(sa) >= 6:
            fe.write(en + "\n")
            fs.write(sa + "\n")

print("BPCC Sanskrit export complete")
