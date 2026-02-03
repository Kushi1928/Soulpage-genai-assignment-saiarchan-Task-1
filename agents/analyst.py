import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyst_agent(data):
    prompt = f"""
You are a financial analyst.

Based on the company data below, generate:
1. Key Insights
2. Growth Opportunities
3. Risk Factors

Company Data:
{data}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text
