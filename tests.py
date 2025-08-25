from functions.run_python_file import run_python_file
# from functions.write_files import write_file

result = run_python_file("calculator", "main.py")
print("Result for: calculator, main.py:\n", result)

result = run_python_file("calculator", "main.py", ["3 + 5"]) 
print("Result for: calculator, main.py:, 3+5\n", result)

result = run_python_file("calculator", "tests.py")
print("Result for: calculator, tests.py:\n", result)

result = run_python_file("calculator", "../main.py")
print("Result for: calculator, ../main.py:\n", result)

result = run_python_file("calculator", "nonexistent.py")
print("Result for: calculator, noneexistent.py:\n", result)

# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print("Result for lorem.txt:\n", result)

# result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print("Result for pkg/morelorem.txt:\n", result)

# result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print("Result for /tmp/temp.txt:\n", result)

# result = get_files_info("calculator", ".")
# print("Result for current directory:\n", result)

# result = get_files_info("calculator", "pkg")
# print("Result for 'pkg' directory:\n", result)

# result = get_files_info("calculator", "/bin")
# print("Result for '/bin' diretory:\n", result)

# result = get_files_info("calculator", "../")
# print("Result for '../' directory:\n", result)

# result = get_file_content("calculator", "main.py")
# print("Result for 'main.py':", result)

# result = get_file_content("calculator", "pkg/calculator.py")
# print("Result for 'pkg/calculator.py':", result)

# result = get_file_content("calculator", "/bin/cat")
# print("Result for '/bin/cat':", result)

# result = get_file_content("calculator", "pkg/does_not_exist.py")
# print("Result for 'pkg/does_not_exist.py':", result)