# create a python program that perfroms as a calculator running in the while loop until terminated

#create different  functions for addition, subtraction, multiplication and division.
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        print("Error! Division by zero is not allowed.")
    else:
        return x / y

print('Welcome to the Python Calculator')
while True:
    print()
    print('Select operation:')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')

