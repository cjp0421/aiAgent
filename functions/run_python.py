import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    allowed_directory = os.path.abspath(working_directory)
    
    if not absolute_file_path.startswith(allowed_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not absolute_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        command = ["python", file_path] + args
        output = subprocess.run(command, cwd=working_directory, capture_output=True, timeout=30)
        stdout = output.stdout.decode()
        stderr = output.stderr.decode()
        
        result = f"STDOUT: {output.stdout.decode()}\nSTDERR: {output.stderr.decode()}"
        if not stdout and not stderr:
            result = "No output produced."
        if output.returncode != 0:
            result = result + f"Process exited with code {output.returncode}"
        print(result)
    except Exception as e:
        return f"Error: executing Python file: {e}"