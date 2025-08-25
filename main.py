import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_functions import call_function
from functions.get_files_info import schema_get_files_info
from functions.get_files_info import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_files import schema_write_files

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_files
    ]
)

def main():
    print("Hello from aiAgent!")
    load_dotenv()
    if len(sys.argv) < 2:
        sys.exit("error: no prompt provided")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    system_prompt = """
    You are a helpful AI coding agent. You have access to tools that let you explore and understand codebases.

    When a user asks a question, you should:
    1. First explore the available files and directories using get_files_info
    2. Read relevant files using get_file_content to understand the code
    3. Then provide a comprehensive answer based on what you discovered

    You can perform the following operations:
    - List files and directories
    - Read file contents  
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. Always start by exploring the codebase to understand what's available before answering questions.
    """

    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    
    client = genai.Client(api_key=api_key)

    for _ in range(20):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                    )
            )

            for candidate in response.candidates:
                messages.append(candidate.content)

            verbose = len(sys.argv) > 2 and sys.argv[2] == '--verbose'
            
            if response.function_calls:
                function_responses = []
                for function_call_part in response.function_calls:
                    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                    result = call_function(function_call_part=function_call_part, verbose=verbose)
                    if not result.parts[0].function_response.response:
                        raise Exception("response is malformed")
                    if verbose:
                        print(f"-> {result.parts[0].function_response.response}")

                    function_responses.append(result.parts[0])
                
                messages.append(types.Content(role="user", parts=function_responses))
            else:
                if verbose:
                    print(f"User prompt: {sys.argv[1]}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")   
                print("Final response:")
                print(f"{response.text}")
                break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
