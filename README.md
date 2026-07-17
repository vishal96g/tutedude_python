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


