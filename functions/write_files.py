import os

def write_file(working_directory, file_path, content):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    allowed_directory = os.path.abspath(working_directory)
    if not absolute_file_path.startswith(allowed_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_file_path):
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