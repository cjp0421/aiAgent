from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")
print("Result for current directory:\n", result)

result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:\n", result)

result = get_files_info("calculator", "/bin")
print("Result for '/bin' diretory:\n", result)

result = get_files_info("calculator", "../")
print("Result for '../' directory:\n", result)