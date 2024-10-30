##Program to find Power of a number input 5 2 output 25

def calculate_power(base, exponent):
    return base ** exponent

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
