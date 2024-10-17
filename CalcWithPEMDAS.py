class Calculator: # this class contains the basic operations of a calculator
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
    print(actionOrder(operation))

def createOperation(operation): # this function takes the user input and creates a list of operands and operators removing any spaces
    operation = operation.replace(' ', '')

    operands = []

    for num in range(len(operation)):
        if operation[num].isdigit():
            operands.append(float(operation[num]))
        else:
            operands.append(operation[num])

    return operands

def actionOrder(operation):
    operands = createOperation(operation)

    op = operands.count('(')
    result = 0

    if op > 0:
        while op != 0:
            for num in range(len(operands)):
                if operands[num] == '(':
                    start = num
                if operands[num] == ')':
                    end = num
                    result = checkOperation(operands[start + 1:end])
                    operands[start] = result
                    for num in range(end - start):
                        operands.pop(start + 1)
                    op -= 1
                    break
        if len(operands) > 1:
            result = checkOperation(operands)
            operands[0] = result
    else:
        result = checkOperation(operands)
        operands[0] = result

    return operands[0]



def checkOperation(operation): 
    operands = operation
    

    result = 0

    mult = operands.count('*')
    div = operands.count('/')
    add = operands.count('+')
    sub = operands.count('-')

    if len(operands) == 1:
        return operands[0]

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

    

        