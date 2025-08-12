import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello from aiagent!")
    load_dotenv()
    if len(sys.argv) < 2:
        sys.exit("error: no prompt provided")
    api_key = os.environ.get("GEMINI_API_KEY")
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=f"{messages}"
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
