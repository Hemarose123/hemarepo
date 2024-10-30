##How Old Are You, Specifically?
##Using if statements, else if, and else statements, make a program which displays a different message depending on the age given.

def age_message(age):
    if age <16:
        return "You can't drive"
    elif age <= 17:
        return "You can drive but not vote"
    elif age <= 24:
        return "You can vote but not rent a car"
    elif age >= 25:
        return "You can do pretty much anything"
    else:
        return "You are a senior citizen."


age = int(input("Enter your age: "))

message = age_message(age)
print(message)
