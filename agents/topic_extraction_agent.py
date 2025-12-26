from groq import Groq
import os
import json
from agents.utils import chunk_list

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an AI agent that extracts high-level product issues,
feature requests, and feedback topics from app reviews.

Rules:
- Topics must be short (2–5 words)
- Merge similar issues conceptually
- Create new topics if needed
- Avoid duplicates
- Return ONLY valid JSON

Output format:
{
  "topics": ["topic 1", "topic 2"]
}
"""

def extract_topics_llm(reviews):
    all_topics = []

    for review_chunk in chunk_list(reviews, chunk_size=20):
        user_prompt = "Reviews:\n" + "\n".join(f"- {r}" for r in review_chunk)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        chunk_topics = json.loads(
            response.choices[0].message.content
        )["topics"]

        all_topics.extend(chunk_topics)

    return all_topics
