##Write a function called factorial that takes a parameter n and returns the factorial of n. Call the factorial function with different values of n and print the result.
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
result1 = factorial(5)
print(f"Factorial of 5 is: {result1}")  # Output will be 120

result2 = factorial(0)
print(f"Factorial of 0 is: {result2}")  # Output will be 1

result3 = factorial(-3)
print(f"Factorial of -3 is: {result3}")  # Output will be an error message
