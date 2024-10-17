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
    print(checkOperation(operation))

def checkOperation(operation):
    operands = operation.split()

    result = 0

    mult = operands.count('*')
    div = operands.count('/')
    add = operands.count('+')
    sub = operands.count('-')

    while mult != 0 or div != 0:
        if mult > 0:
            for num in range(len(operands)):
                if operands[num] == '*':
                    result = calc.multiply(float(operands[num - 1]), float(operands[num + 1]))
                    operands[num] = result
                    operands.pop(num + 1)
                    operands.pop(num - 1)
                    mult -= 1
                    break
        if div > 0:
            for num in range(len(operands)):
                if operands[num] == '/':
                    result = calc.divide(float(operands[num - 1]), float(operands[num + 1]))
                    operands[num] = result
                    operands.pop(num + 1)
                    operands.pop(num - 1)
                    div -= 1
                    break
    while add != 0 or sub != 0:
        if add > 0:
            for num in range(len(operands)):
                if operands[num] == '+':
                    result = calc.add(float(operands[num - 1]), float(operands[num + 1]))
                    operands[num] = result
                    operands.pop(num + 1)
                    operands.pop(num - 1)
                    add -= 1
                    break
        if sub > 0:
            for num in range(len(operands)):
                if operands[num] == '-':
                    result = calc.subtract(float(operands[num - 1]), float(operands[num + 1]))
                    operands[num] = result
                    operands.pop(num + 1)
                    operands.pop(num - 1)
                    sub -= 1
                    break
    return result





main()

    

        