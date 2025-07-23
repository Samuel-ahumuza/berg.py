num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
sum_result= num1 +num2
print(f"sum:{num1+num2}= {sum_result}")

num3 =float(input("Enter the dividend for division:"))
num4 = float(input("Enter the divisor for division:"))
div_result= num3/num4
if num4 == 0:
    print("Error. Division by 0 is not allowed")
else:
    print(f"(Division:{num3/num4} = {div_result})")

base= float(input("Enter the length of the base of the triangle:"))
height= float(input("Enter the height of the triangle:"))
area= 0.5*base*height
print(f"(The are of the triangle is:{area}")

a=float(input("Enter the first variable:"))
float(input("Enter the second variable:"))
print(f"Original values: a= {a}, b={b}")
print(f"Swapped values: a={b}, b={a}")
import random
print(f"Random number: {random.randint(1,100)}")

kilometers= float(input("Enter distance in kilometeres:"))
conversion_factor=0.621371
miles=kilometers*conversion_factor
print(f"Kilometers is equal to {miles} miles")

celsius =float(input("Enter the temperature in celsius:"))
fahrenheit = (celsius *9/5)+32
print(f"The temprature in fahrenheit: ={fahrenheit} degrees fahrenheit")

import calendar
year=int(input("Enter year:"))
month=int(input("Enter month:"))
cal=calendar.month(year,month)
print(f"calendar: = {cal}")

a=float(input("Enter the number:"))
if a > 0:
    print("The number is a positive number.")
elif a == 0:
    print("The number is zero.")
else:
    print("The number is a negative number.")
