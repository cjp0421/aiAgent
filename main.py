import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello from aiAgent!")
    load_dotenv()
    if len(sys.argv) < 2:
        sys.exit("error: no prompt provided")
    api_key = os.environ.get("GEMINI_API_KEY")
    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=f"{messages}"
    )

    if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"{response.text}")

    else:
        print(f"{response.text}")

if __name__ == "__main__":
    main()
