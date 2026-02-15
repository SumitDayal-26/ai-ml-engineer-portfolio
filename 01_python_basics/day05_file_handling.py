# Day 5: File Handling in Python
#1. Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is my first file.\n")
    file.write("Learning Python for AI/ML.\n")
print(" Data written to file sucessfully.")

#2. Reading from a file
with open("sample.txt", "r") as file:
    content=file.read()
print("\n reading from file:")
print(content)

