"""Welcome To The Grading Scale"""
score = int(input("score 0 <= 100:"))
if 80 <=score<= 100:
    print("D1")
elif 70 <=score<= 79:
    print("D2")
elif 65 <=score<= 69:
    print("C3")
elif 60 <=score<= 64:
    print("C4")
elif 55 <=score<= 59:
    print("C5")
elif 50 <=score<= 54:
    print("C6")
elif 45 <=score<= 49:
    print("P7")
elif 40 <=score<= 44:
    print("P8")
elif 0 <=score<= 39:
    print("F9")
else:
    print("Invalid input. Please enter score between 0 and 100")
