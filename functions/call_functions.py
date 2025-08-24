import os
from functions.get_files_info import get_file_content, get_files_info
from functions.run_python import run_python_file
from functions.write_files import write_file
from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python": run_python_file,
        "write_file": write_file,
    }

    try:
        function_to_run = function_map[function_call_part.name]
    except Exception:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    function_call_part.args["working_directory"] = "./calculator"
    
    function_result = function_to_run(**function_call_part.args)

    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )