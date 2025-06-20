def calculate_average(numbers):
    sum = 0
    for number in numbers:
     sum += number
    average = sum / len(numbers)
    return average
numbers = [12, 8, 16, 4, 20]
average = calculate_average(numbers)
print("Average:", average)