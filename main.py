import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_files_info import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_files import schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

def main():
    print("Hello from aiAgent!")
    load_dotenv()
    if len(sys.argv) < 2:
        sys.exit("error: no prompt provided")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=f"{messages}",
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
            )
    )

    
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    elif len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")   
        print(f"{response.text}")

    else:
        print(f"{response.text}")

if __name__ == "__main__":
    main()
