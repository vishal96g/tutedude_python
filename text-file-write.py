# Program to create a text file and write user-provided content

# Ask the user for the file name
filename = input("Enter the file name (e.g., notes.txt): ")

# Ask the user for the content
content = input("Enter the content you want to write into the file: ")

# Open the file in write mode and write the content
with open(filename, "w") as file:
    file.write(content)

print(f"Content written to {filename} successfully.")
