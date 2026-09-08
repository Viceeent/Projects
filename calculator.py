history = []
num1 = 0
num2 = 0
op = ['1.add', '2.subtract', '3.divide', '4.multiply', '5.power', '6.modulus', '7.floor division', '8.show history', '9.clear history', '10.QUIT' ]
#All the functions
def add(num1,num2):
    num1 = float(input('Whats your first number? '))
    num2 = float(input('Whats your second number? '))
    result = num1 + num2
    history.append(result)
    return result
def subtract(num1,num2):
    num1 = float(input('Whats your first number? '))
    num2 = float(input('Whats your second number? '))
    result = num1 - num2
    history.append(result)
    return result
def divide(num1,num2):
    num1 = float(input('Whats your first number? '))
    num2 = float(input('Whats your second number? '))
    if num2 == 0:
        print('You cant divide by 0')
    else:
        result = num1 / num2
        history.append(result)
        return result
def multiply(num1,num2):
    num1 = float(input('Whats your first number? '))
    num2 = float(input('Whats your second number? '))
    result = num1 * num2
    history.append(result)
    return result
def power(num1,num2):
    num1 = float(input('Whats your first number?'))
    num2 = int(input('Whats the power? '))
    result = num1 ** num2
    history.append(result)
    return result
def modulus(num1,num2):
    num1 = float(input('Whats your dividend? '))
    num2 = float(input('Whats your divisor? '))
    result = num1 % num2
    history.append(result)
    return result
def floordivision(num1,num2):
    num1 = float(input('Whats your first number? '))
    num2 = float(input('Whats your second number? '))
    if num2 == 0:
        print('You cant divide by 0')
    else:
        result = num1 // num2
        history.append(result)
        return result
def showhistory(history):
    for item in history:
        print(item)
def clearhistory(history):
    history.clear()

print('Welcome to My calculator!!!')
while True:
    print('What operation would you like to do?')
    for item in op:
        print(item)
    operation = int(input('please input the number next to the function: '))
    if operation == 1:
        print(add(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 2:
        print(subtract(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 3:
        print(divide(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 4:
        print(multiply(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 5:
        print(power(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 6:
        print(modulus(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 7:
        print(floordivision(num1,num2))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 8:
        print(showhistory(history))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 9:
        print(clearhistory(history))
        exit = input('Wanna exit (y/n): ')
        if exit == 'y':
            break
    elif operation == 10:
        break
print('Thanks For using our services!!!!')
    
