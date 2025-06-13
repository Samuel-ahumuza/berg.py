"""Welcome To The Grading Scale"""
score = int(input("score 0 <= 100:"))
if 90 <=score<= 100:
    print("D1")
elif 80 <=score<= 89:
    print("D2")
elif 70 <=score<= 79:
    print("C3")
elif 60 <=score<= 69:
    print("C4")
elif 50 <=score<= 59:
    print("C5")
elif 40 <=score<= 49:
    print("C6")
elif 30 <=score<= 39:
    print("P7")
elif 20 <=score<= 29:
    print("P8")
elif 0 <=score<= 19:
    print("F9")
else:
    print("Invalid input. Please enter score between 0 and 100")