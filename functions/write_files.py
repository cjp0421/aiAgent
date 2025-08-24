import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file, constrained to the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    allowed_directory = os.path.abspath(working_directory)
    if not absolute_file_path.startswith(allowed_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)
    except Exception as e:
        return f"Error: {str(e)}"
    
    try:
        with open(absolute_file_path, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"