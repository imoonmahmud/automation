import json
from llm import ask_llm


def classify_message(text):
    prompt = f"""Classify the following customer message into exactly one word: sales, support, or billing.
    Reply with only that one word, nothing else.

    Message: "{text}" """

    reply = ask_llm(prompt)
    if reply is None:
        return 'unknown'

    reply = reply.strip().lower()
    if reply not in ('sales', 'support', 'billing'):
        return 'unknown'
    return reply

def extract_lead_info(text):
    prompt = f"""Extract the following fields from this message as JSON only, no other text:
    - name (string, or null if not mentioned)
    - product (string, or null if not mentioned)
    - budget (number, or null if not mentioned)

    Message: "{text}"

    Reply with only valid JSON, like: {{"name": null, "product": null, "budget": null}}"""

    reply = ask_llm(prompt)
    if reply is None:
        return None

    reply = reply.strip()
    if reply.startswith("```"):
        reply = reply.strip('`')
        reply = reply.replace('json', '', 1).strip()

    try:
        return json.loads(reply)
    except json.JSONDecodeError:
        return None
