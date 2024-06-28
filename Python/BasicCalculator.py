# Make a basic calculator
# That prints:
# addition, subtraction, multiplication, division, and modulo
# with the number prompt int a = 15, int b = 5
# start the program by printing:
# 1st line = 'This is a basic calculator!'
# operator line = 'Addition: ...' (and so on along with other operator)

print("This is a basic calculator!")

a = 15
b = 5

def addition(a, b):
    sum = a + b
    return sum

def subtraction(a, b):
    difference = a - b
    return difference

def multiplication(a, b):
    product = a * b
    return product

def division(a, b):
    divided = a / b
    return divided

def modulo(a, b):
    remainder = a % b
    return remainder

print("number a = " + str(a) + ", number b = " + str(b))
print("Addition: " + str(addition(a, b)))
print("Subtraction: " + str(subtraction(a, b)))
print("Multiplication: " + str(multiplication(a, b)))
print("Division: " + str(division(a, b)))
print("Modulo: " + str(modulo(a, b)))

# made in python, 30 lines of code