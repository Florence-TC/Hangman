student_score = int(input())
max_score = int(input())

percentage = student_score / max_score * 100

if percentage < 60:
    print("F")
elif percentage < 70:
    print("D")
elif percentage < 80:
    print("C")
elif percentage < 90:
    print("B")
else:
    print("A")
