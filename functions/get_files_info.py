import os

def get_files_info(working_directory, directory="."):
    fullPath = os.path.join(working_directory, directory)

    absolutePath = os.path.abspath(fullPath)
    wdAbsolutePath = os.path.abspath(working_directory)

    if not absolutePath.startswith(wdAbsolutePath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolutePath):
        return f'Error: "{directory}" is not a directory'
    
    # print(f"{os.listdir(absolutePath)}")

    for pathPart in os.listdir(absolutePath):
        # print(pathPart)
        # partFullPath = f"{absolutePath}/{pathPart}"
        partFullPath = os.path.join(absolutePath,pathPart)
        print(f"- {pathPart}: file_size={os.path.getsize(partFullPath)} bytes, is_dir={os.path.isdir(partFullPath)}")
