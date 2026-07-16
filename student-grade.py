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

