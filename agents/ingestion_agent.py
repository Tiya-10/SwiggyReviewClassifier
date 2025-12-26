import json
from collections import defaultdict

def load_daily_batches(file_path):
    """
    Returns:
    {
      "2024-06-01": [review1, review2, ...],
      "2024-06-02": [...]
    }
    """
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    daily_batches = defaultdict(list)

    for r in reviews:
        daily_batches[r["date"]].append(r["review"])

    return dict(daily_batches)


