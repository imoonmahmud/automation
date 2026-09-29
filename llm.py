import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('GROQ_API_KEY')
if not key:
    raise SystemExit("Missing GROQ_API_KEY in .env")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"}
payload = {
    "model": "openai/gpt-oss-120b",
    "messages": [{"role": "user", "content": "Say hello in one short sentence."}]}


def ask_llm(prompt):
    response = requests.post(url, headers=headers, json={
        "model": "openai/gpt-oss-120b",
        "messages": [{"role": "user", "content": prompt}]
    })
    if response.status_code != 200:
        return None
    return response.json()['choices'][0]['message']['content']
