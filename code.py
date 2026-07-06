!pip install -q transformers datasets sentencepiece


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

insight_generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_health_insight(data_summary):
    prompt = f"""
You are a public health analytics expert. Given the hospital data below, generate 3 data-driven insights that highlight trends, anomalies, or areas needing attention. Write in a professional tone.

Hospital Data:
{data_summary}
"""
    result = insight_generator(prompt, max_length=300, do_sample=False)[0]['generated_text']
    return result


hospital_data_summary = """
- Average OPD patient count over last 7 days: 820
- Vaccination no-shows this week: 45%
- Complaint spike: 30% increase in fever and flu-like symptoms
- Rural footfall up by 25% due to seasonal migration
- 18% of patients are repeat visits in last 10 days
- Highest traffic: Monday, 10AM–12PM
"""


insights = generate_health_insight(hospital_data_summary)
print("Public Health Insights:\n")
print(insights)
