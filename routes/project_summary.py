from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_project_summary(results):

    prompt = f"""
You are a senior software architect.
Analyze the following project scan results and produce a health report.

Results:
{results}

Return:

Project Health Score (0–100)
Security Risk Level
Main Problems
Recommendations
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
