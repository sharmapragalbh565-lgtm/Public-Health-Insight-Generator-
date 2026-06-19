# Public Health Insight Generation using LLMs

This project uses a large language model (LLM) to generate concise, actionable insights from structured hospital summary data. It is designed to support healthcare administrators and public health officials in identifying trends, resource gaps, and potential health risks using natural language generation.

---

## Features

- Converts tabular or summarized hospital data into human-readable insights
- Provides early warnings, utilization trends, and strategic suggestions
- Uses Google's Flan-T5 Large model for inference
- Supports structured prompt formatting for consistent recommendations
- Includes evaluation metrics: ROUGE, BLEU, BERTScore

---

## Use Cases

- Weekly hospital reporting automation
- Public health monitoring for government hospitals
- Support for policy decisions in healthcare administration
- Integration with dashboards for live health analytics

---

## Tech Stack

- Python
- Hugging Face Transformers
- Google Flan-T5 (Instruction-tuned LLM)
- Google Colab for execution and testing
- NLP metrics: ROUGE, BLEU, BERTScore

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/public-health-insight-model.git
cd public-health-insight-model
