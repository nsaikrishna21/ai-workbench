import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found")
    print("Copy .env.example to .env and update with your OpenAI API key")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL= os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# -the call--
print("Sending prompt: What is Gen Ai in one sentence?")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You're helpful assistant. Be concise"},
            {"role": "user", "content": "What is Gen Ai in one sentence?"},
        ],
        temperature=0.7,
        max_tokens=100,
    )

# response + errors

    print(f"Response: {response.choices[0].message.content}")
    print(f"Token usage: {response.usage}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Completion tokens: {response.usage.completion_tokens}")
    print(f"Total tokens: {response.usage.total_tokens}")

except AuthenticationError:
    print("Error: Invalid API key. Check your .env file")
except APIConnectionError:
    print("Error: Cannot connect. Check your internet connection")
except Exception as e:
    print(f"UnexpectedError: {e}")