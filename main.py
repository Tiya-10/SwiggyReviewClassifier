import pandas as pd
from agents.ingestion_agent import load_daily_batches
from agents.trend_agent import process_daily_batch_llm

DATA_PATH = "data/raw_reviews/swiggy_reviews.json"

daily_batches = load_daily_batches(DATA_PATH)

trend_data = {}
all_topics = set()

for date, reviews in daily_batches.items():
    canonical_topics, counts = process_daily_batch_llm(reviews)
    trend_data[date] = counts
    all_topics.update(canonical_topics)

df = pd.DataFrame(index=sorted(all_topics))

for date, counts in trend_data.items():
    df[date] = df.index.map(lambda x: counts.get(x, 0))

df = df.fillna(0).astype(int)

df.to_csv("output/reports/trend_report.csv")
print(df)
