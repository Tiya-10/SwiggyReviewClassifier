from collections import Counter
from agents.topic_extraction_agent import extract_topics_llm
from agents.dedup_agent import deduplicate_topics_llm
from agents.taxonomy_store import load_taxonomy, save_taxonomy

def process_daily_batch_llm(reviews):
    extracted_topics = extract_topics_llm(reviews)

    existing_taxonomy = load_taxonomy()
    combined_topics = list(set(existing_taxonomy + extracted_topics))

    canonical_topics = deduplicate_topics_llm(combined_topics)
    save_taxonomy(canonical_topics)

    topic_counts = Counter(extracted_topics)

    return canonical_topics, topic_counts
