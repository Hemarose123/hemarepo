##Program to identify if the  number is positive or negative


def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
result1 = check_number(5)
print(result1)  # Output will be "The number is positive."

result2 = check_number(-3)
print(result2)  # Output will be "The number is negative."

result3 = check_number(0)
print(result3)  # Output will be "The number is zero."
