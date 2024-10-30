##Write a Python program that determines if a given year is a leap year.Enter a year as input. Use conditional statements to check if the year satisfies the leap year conditions: 
##The year should be divisible by 4 but not divisible by 100, or The year should be divisible by 400. 
##Use appropriate logical operators and conditions to implement the leap year logic. 
##Display an appropriate message indicating whether the year is a leap year or not. 


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter the year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
