# Tutedude Python Practical

**Description:**
- Python program to check score and print grade using if-else.
- Dictionary-based program to add, update, and print student grades with if-else.
- Program to create a text file and write user input using open() and write().
- Program to read a text file in read mode and display content using file.read().

**Author:** Vishal Gupta




## ✨ Python program to check score and print grade using if-else.
#### 1. A Python program that takes a score as input and prints the grade based on defined ranges (A–F). It uses basic if-else statements to evaluate the marks.


**File:** `student-grade.py`  
```
## Program to calculate grade based on score

# Take score as input
score = int(input("Enter your score: "))

# Check conditions and print grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
<img width="1265" height="501" alt="image" src="https://github.com/user-attachments/assets/7c1bf6a8-e90a-408f-b359-b394a0b090de" />

## ✨ Dictionary-based program to add, update, and print student grades with if-else.
#### 2. A dictionary-based Python program where student names are keys and grades are values. It allows adding new students, updating existing grades, and printing all student records using dictionary operations and if-else logic.


**File:** `dictionary-program.py`  
```
# Student Grades Dictionary Program

students = {}  # Empty dictionary to store student names and grades

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"{name} added with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"Student {name} not found.")

    elif choice == "3":
        if students:
            print("\n--- Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
```
<img width="1050" height="862" alt="image" src="https://github.com/user-attachments/assets/8a3aa455-fdb0-4894-a3c2-c4ed94b56542" />

## ✨ Program to create a text file and write user input using open() and write()
#### 3. A Python program that creates a text file and writes user-provided content into it using file handling functions like open() and write().


**File:** ` text-file-write.py`  
```
# Program to create a text file and write user-provided content

# Ask the user for the file name
filename = input("Enter the file name (e.g., notes.txt): ")

# Ask the user for the content
content = input("Enter the content you want to write into the file: ")

# Open the file in write mode and write the content
with open(filename, "w") as file:
    file.write(content)

print(f"Content written to {filename} successfully.")
```
<img width="1242" height="225" alt="image" src="https://github.com/user-attachments/assets/6b7281a6-469c-420a-a1f7-1ee0558653b9" />

