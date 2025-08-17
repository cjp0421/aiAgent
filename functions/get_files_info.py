import os

from config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    fullPath = os.path.join(working_directory, directory)

    absolutePath = os.path.abspath(fullPath)
    wdAbsolutePath = os.path.abspath(working_directory)

    if not absolutePath.startswith(wdAbsolutePath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolutePath):
        return f'Error: "{directory}" is not a directory'

    files = []

    try:
        for pathPart in os.listdir(absolutePath):
            partFullPath = os.path.join(absolutePath,pathPart)
            files.append(f"- {pathPart}: file_size={os.path.getsize(partFullPath)} bytes, is_dir={os.path.isdir(partFullPath)}")

        return "\n".join(files)
    except Exception as e:
        return f"Error: {str(e)}"

def get_file_content(working_directory, file_path):    
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    allowed_directory = os.path.abspath(working_directory)
    
    if not absolute_file_path.startswith(allowed_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(absolute_file_path, "r") as file:
            file_content_str = file.read()
            if len(file_content_str) > MAX_CHARS:
                return file_content_str[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            else:
                return file_content_str
    except Exception as e:
        return f"Error: {str(e)}"
