##Write a program that takes two numbers as input and prints which one is greater (or if they are equal) using if-else statements.


def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num2} is greater than {num1}.")
    else:
        print("Both numbers are equal.")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
compare_numbers(number1, number2)
