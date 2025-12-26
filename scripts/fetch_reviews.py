from google_play_scraper import Sort, reviews
import json
from datetime import datetime

APP_ID = "in.swiggy.android"
START_DATE = datetime(2024, 6, 1)
MAX_REVIEWS = 3000   # 🔥 LIMIT (important)

def fetch_reviews_limited():
    all_reviews = []
    continuation_token = None

    while len(all_reviews) < MAX_REVIEWS:
        result, continuation_token = reviews(
            APP_ID,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )

        for r in result:
            review_date = r["at"]

            if review_date < START_DATE:
                return all_reviews

            all_reviews.append({
                "date": review_date.strftime("%Y-%m-%d"),
                "review": r["content"],
                "rating": r["score"]
            })

            if len(all_reviews) >= MAX_REVIEWS:
                break

        print(f"Fetched {len(all_reviews)} reviews...")

        if continuation_token is None:
            break

    return all_reviews


if __name__ == "__main__":
    data = fetch_reviews_limited()

    with open("data/raw_reviews/swiggy_reviews.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved {len(data)} reviews successfully")
