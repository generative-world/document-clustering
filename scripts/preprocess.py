import os
import json

def preprocess_contracts(data_dir):
    """Preprocess contract files for training."""
    contracts = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as file:
                contracts.append(file.read())
    return contracts

if __name__ == "__main__":
    contracts = preprocess_contracts("data/sample_contracts")
    with open("data/preprocessed_contracts.json", "w") as f:
        json.dump(contracts, f)
