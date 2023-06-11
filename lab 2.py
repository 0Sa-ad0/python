#1
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def calculate_average_marks(course_marks):
    return sum(course_marks) / len(course_marks)

course_names = ['Course 1', 'Course 2', 'Course 3', 'Course 4', 'Course 5', 'Course 6', 'Course 7', 'Course 8']
course_marks = []

for course in course_names:
    marks = float(input(f"Enter marks for {course}: "))
    course_marks.append(marks)

average_marks = calculate_average_marks(course_marks)

print("Course-wise grades:")
for i in range(len(course_names)):
    print(f"{course_names[i]}: {calculate_grade(course_marks[i])}")

print(f"\nAverage Marks: {average_marks}")
print(f"Grade: {calculate_grade(average_marks)}")

#2
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = width * height

print("The area of the rectangle is:", area)

#3
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

perimeter = 2 * (width + height)

print("The perimeter of the rectangle is:", perimeter)

#4
import math

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

diagonal = math.sqrt(width**2 + height**2)

print("The diagonal length of the rectangle is:", diagonal)

#5
import math

area = float(input("Enter the area of the rectangle: "))
side = float(input("Enter the length of one side of the rectangle: "))

other_side = area / side

print("The length of the other side of the rectangle is:", other_side)



#6
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("The temperature in Celsius is:", celsius)


#7
celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("The temperature in Fahrenheit is:", fahrenheit)

#8
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#9
def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

num_terms = int(input("Enter the number of terms: "))

fibonacci = fibonacci_sequence(num_terms)

print("The Fibonacci sequence:")
print(fibonacci)

#10
def fibonacci(n):
    if n <= 0:
        return None  
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  

    prev1, prev2 = 0, 1
    fib = None
    for _ in range(3, n + 1):
        fib = prev1 + prev2
        prev1, prev2 = prev2, fib

    return fib

num = int(input("Enter a number: "))

fibonacci_value = fibonacci(num)

if fibonacci_value is None:
    print("Invalid input! Please enter a positive integer.")
else:
    print(f"The Fibonacci value of {num} is:", fibonacci_value)
    
 #11  
def is_palindrome(number):
    num_digits = 0
    temp = number
    while temp > 0:
        num_digits += 1
        temp //= 10

    reverse = 0
    temp = number
    for _ in range(num_digits):
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp //= 10

    return number == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    
#12
def calculate_triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = calculate_triangle_area(base, height)

print("The area of the triangle is:", area)



