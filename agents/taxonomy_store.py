import json
import os

TAXONOMY_FILE = "data/taxonomy.json"

def load_taxonomy():
    if not os.path.exists(TAXONOMY_FILE):
        return []
    with open(TAXONOMY_FILE, "r") as f:
        return json.load(f)

def save_taxonomy(topics):
    with open(TAXONOMY_FILE, "w") as f:
        json.dump(sorted(set(topics)), f, indent=2)
