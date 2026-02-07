from datasets import load_dataset

ds = load_dataset(
    "ai4bharat/BPCC",
    "bpcc-seed-latest",
    split="san_Deva"
)

print("Number of English–Sanskrit pairs:", len(ds))
