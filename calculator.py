# create a python program that perfroms as a calculator running in the while loop until terminated

#create different  functions for addition, subtraction, multiplication and division.

#function to add two numbers
def add(first_number,second_number):
    answer = first_number + second_number
    return answer

#function to substract two numbers
def subtract(first_number,second_number):
    return first_number - second_number

#fuction to multiply two numbers
def multiply(first_number,second_number):
    return first_number * second_number

#function to divide two numbers
def divide(first_number,second_number):
    if y == 0:
        print("Error! Division by zero is not allowed.")
    else:
        return first_number / second_number

print('Welcome to the Python Calculator')
print("kindly enter 'start' to start the calculator or enter end to exit")

start_stop = input()

if start_stop == 'start':
    cal_start = True
elif start_stop == 'end':
    exit()

while cal_start == True:
    #enter the first number
    first_number = int(input("Enter the first number: "))

    #print different types of operations
    #select one of them
    print('Select operation:')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')

    choice = int(input("Kindly select operations from the above options "))

    if choice == 1:
        second_number = int(input("Enter the second number: "))
        print(add(first_number,second_number))
    elif choice == 2:
        second_number = input("Enter the second number: ")
        print(subtract())
    if choice == 3:
        second_number = input("Enter the second number: ")
        print(multiply())
    if choice == 4:
        second_number = input("Enter the second number: ")
        print(divide())
    print("kindly enter 'start' to start the calculator again or enter end to exit")

    if input() == 'start':
        cal_start == True
    else:
        cal_start == False
        exit("Nothing")




