from groq import Groq
import os
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an AI agent responsible for consolidating topic names.

Given a list of topics:
- Merge topics referring to the same underlying issue
- Choose the best canonical name
- Do NOT over-merge unrelated topics
- Keep names short and clear

Return ONLY valid JSON.

Output format:
{
  "canonical_topics": ["topic 1", "topic 2"]
}
"""

def deduplicate_topics_llm(topics):
    user_prompt = "Topics:\n" + "\n".join(f"- {t}" for t in topics)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)["canonical_topics"]
