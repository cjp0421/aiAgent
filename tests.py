from functions.get_files_info import get_file_content, get_files_info

result = get_files_info("calculator", ".")
print("Result for current directory:\n", result)

result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:\n", result)

result = get_files_info("calculator", "/bin")
print("Result for '/bin' diretory:\n", result)

result = get_files_info("calculator", "../")
print("Result for '../' directory:\n", result)

result = get_file_content("calculator", "main.py")
print("Result for 'main.py':", result)

result = get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg/calculator.py':", result)

result = get_file_content("calculator", "/bin/cat")
print("Result for '/bin/cat':", result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for 'pkg/does_not_exist.py':", result)