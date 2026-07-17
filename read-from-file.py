# Program to read from a file and display content

# Ask the user for the file name
filename = input("Enter the file name to read: ")

try:
    # Open the file in read mode
    file = open(filename, "r")

    # Read the entire content
    content = file.read()

    # Print the content
    print("\n--- File Content ---")
    print(content)

    # Close the file
    file.close()

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

