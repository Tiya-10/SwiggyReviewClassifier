# App Review Trend Analysis using Agentic LLMs

## Overview
This project implements an **Agentic AI system** to analyze Google Play Store reviews and generate **topic-wise trend reports** over time.  
The system processes app reviews as **daily batches**, extracts high-level issues, requests, and feedback using a **Large Language Model (LLM)**, consolidates semantically similar topics, and produces a **trend table** suitable for product analysis.

The solution is designed to handle:
- High variability in user language
- Semantically similar feedback expressed differently
- Emergence of new and evolving topics over time

---

## Approach
A **multi-agent LLM-based architecture** is used instead of traditional topic modeling techniques.

### Agent Responsibilities
- **Ingestion Agent**: Loads and groups reviews into daily batches  
- **Topic Extraction Agent (LLM)**: Dynamically identifies high-level topics from reviews  
- **Deduplication Agent (LLM)**: Merges semantically equivalent topics into a canonical taxonomy  
- **Taxonomy Store**: Maintains persistent topic memory across days  
- **Trend Agent**: Builds topic frequency trends over time  

This agentic approach ensures **high recall**, prevents topic fragmentation, and adapts to evolving user feedback.

---

## LLM Details
- **Provider**: Groq  
- **Model**: `llama-3.1-8b-instant`  
- Reviews are processed in **small chunks** to stay within token limits and improve reliability.

---

## Project Structure
```

review_trend_agent/
├── agents/
│   ├── ingestion_agent.py
│   ├── topic_extraction_agent.py
│   ├── dedup_agent.py
│   ├── taxonomy_store.py
│   └── trend_agent.py
├── data/
│   ├── raw_reviews/
│   │   └── swiggy_reviews.json
│   └── taxonomy.json
├── output/
│   └── reports/
│       └── trend_report.csv
├── scripts/
│   └── fetch_reviews.py
├── main.py
├── requirements.txt
└── README.md

````

---

## Output
The system generates a **CSV trend report** where:
- **Rows** represent topics  
- **Columns** represent dates (daily)  
- **Values** represent topic frequency on that date  

This report enables product teams to identify **recurring issues and emerging trends**.

---

## Setup & Run

### 1. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install groq
```

### 3. Set API key (Windows CMD)

```cmd
set GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run

```bash
python main.py
```

---

## Data Source

* Reviews are collected from **Google Play Store**
* Reviews from **June 1, 2024 onward**
* Daily batch processing simulates real-world ingestion

---

## Key Design Choice

**Agentic LLMs are used instead of traditional topic models** because they can reason over context, dynamically create and merge topics, and maintain a consistent evolving taxonomy—resulting in more accurate and actionable trend analysis.

---

## Author

Tiya Tyagi
