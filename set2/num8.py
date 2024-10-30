##Simple Calculator: Implement a basic calculator.
def calculator(num1,num2,operation):
    if operation=="add":
        return num1+num2
    elif operation=="subtract":
        return num1-num2 
    elif operation=="multiply":
        return num1*num2
    elif operation=="divide":
        return num1//num2
    else:
        return "invalid operation"
num1=15
num2=5
print("addition:",calculator(num1,num2,"add"))
print("substraction:",calculator(num1,num2,"substract"))
print("multiplication:",calculator(num1,num2,"multiply"))
print("division",calculator(num1,num2,"divide"))