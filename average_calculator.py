def calculate_average(numbers):
 total = 0
 for number in numbers:
     total += number
 else:
    average = total / len(numbers)
    return average

def classify_average(average):
 if average >= 90:
   return "A"
 elif average >= 80:
   return "B"
 elif average >= 70:
    return "C"
 elif average >= 60:
    return "D"
 elif average <= 59:
    return "F"
 else:
    return ("Invalid, please enter score")
student_scores = [95, 88, 72, 65, 79]
average_score = calculate_average(student_scores)
letter_grade = classify_average(average_score)
print("Average Score:", average_score)
print("Letter Grade:", letter_grade)