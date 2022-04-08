def display():
    print('''
    Select Operator
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage
    ''')

def condition():
    oprtr = float(input('> '))
    
    if oprtr == 1:
        addition()

    if oprtr == 2:
        subtraction()

    if oprtr == 3:
        multiplication()

    if oprtr == 4:
        division()

    if oprtr == 5:
        percentage()

def addition():
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    print('= ', num1+num2)

def subtraction():
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    print('= ', num1-num2)

def multiplication():
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    print('= ', num1*num2)

def division():
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    print('= ', num1/num2)

def percentage():
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    percentage = (num1/100)*num2
    print('=', percentage, '%', 'is', num1, '%' ,'of', num2)

display()
condition()