class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

calc = Calculator()

def main():
    operation = input("Enter the operation: ")
    checkOperation(operation)

def checkOperation(operation):
    operands = operation.split()

    for num in range(len(operands)):
        if operands[num] == '+':
            print(calc.add(int(operands[num - 1]), int(operands[num + 1])))
        elif operands[num] == '-':
            print(calc.subtract(int(operands[num - 1]), int(operands[num + 1])))
        elif operands[num] == '*':
            print(calc.multiply(int(operands[num - 1]), int(operands[num + 1])))
        elif operands[num] == '/':
            print(calc.divide(int(operands[num - 1]), int(operands[num + 1])))
        else:
            pass
main()

    

        