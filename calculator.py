num1 = 0
num2 = 0
op = ['1.add', '2.subtract', '3.divide', '4.multiply', '5.power', '6.modulus', '7.floor division', '8.show history', '9.clear history', '10.QUIT' ]
#All the functions
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        return num1 + num2
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return None
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def power(self, num1, num2):
        return num1 ** num2
    def modulus(self, num1, num2):
        return num1 % num2
    def floordivision(self, num1, num2):
        if num2 != 0:
            return num1 // num2
        else:
            return None
    def show_history(self):
        for item in self.history:
            print(item)
    def clear_history(self):
        self.history.clear()
if __name__ == "__main__":
    calc = Calculator()
    operations = {
        1: calc.add,
        2: calc.subtract,
        3: calc.divide,
        4: calc.multiply,
        5: calc.power,
        6: calc.modulus,
        7: calc.floordivision,
    }

    print('Welcome to My calculator!!!')
    while True:
        print('What operation would you like to do?')
        for item in op:
            print(item)
        operation = int(input('please input the number next to the function: '))

        if operation in operations:
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
            result = operations[operation](num1, num2)
            if result is not None:
                calc.history.append(result)
                print(result)
            else:
                print("There was an issue, nothing has been appended.")
            exit = input('Wanna exit (y/n): ')
            if exit == 'y':
                break
        elif operation == 8:
            calc.show_history()
            exit = input('Wanna exit (y/n): ')
            if exit == 'y':
                break
        elif operation == 9:
            calc.clear_history()
            exit = input('Wanna exit (y/n): ')
            if exit == 'y':
                break
        elif operation == 10:
            break
    print('Thanks For using our services!!!!')