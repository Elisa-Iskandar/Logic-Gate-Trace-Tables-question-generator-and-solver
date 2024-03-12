import random
import re
inputs = ["A","B","C"]
gates = ["AND","OR","XOR","NAND"]
expression = ""
def AND(input1,input2):
    if input1 == 1 and input2 == 1:
        return 1
    else:
        return 0
    
def OR(input1,input2):
    if input1 == 1 or input2 ==1:
        return 1
    else:
        return 0

def NOT(input1):
    if input1 == 1:
        return 0
    else:
        return 1
    
def XOR(input1,input2):
    if (input1 ==1 and input2 ==1) or (input1 == 0 and input2 == 0):
        return 0
    else:
        return 1

def NAND(input1,input2):
    return NOT(AND(input1,input2))

def generate_subexpression():
    subexpression = ""
    for x in range(2):
        temp = random.randint(0,1)
        if temp == 1:
            subexpression += "(NOT("
            subexpression += random.choice(inputs) + "))"
        else:
            subexpression += "(" + random.choice(inputs) + ")"
        if x == 0:
            subexpression += random.choice(gates)
    return subexpression

def generate_expression():
    expression = ""
    for x in range(3):
        expression += "(" + generate_subexpression() + ")"
        if x < 2:
            expression += random.choice(gates)
    return expression

expression = generate_expression()

print("Complete the tracetable for X="+expression+".")
# print("|  A  |  B  |  C  |  X  |")
# print("|-----------------------|")
# print("|  1  |  1  |  1  |     |")
# print("|  1  |  1  |  0  |     |")
# print("|  1  |  0  |  1  |     |")
# print("|  1  |  0  |  0  |     |")
# print("|  0  |  1  |  1  |     |")
# print("|  0  |  1  |  0  |     |")
# print("|  0  |  0  |  1  |     |")
# print("|  0  |  0  |  0  |     |")

def solve(expression):
    temp = re.sub(r'\(+|\)+', ' ', expression)
    operators = list(temp.split(" "))
    operators.pop(0)
    operators.pop(-1)

    results = []
    values = [[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]]
    temp2 = None

    for x in range(len(values)):
        for y in range(len(operators)):
            if operators[y] == "A":
                operators[y] = values[x][0]
            elif operators[y] == "B":
                operators[y] = values[x][1]
            elif operators[y] == "C":
                operators[y] = values[x][2]

        count = 0
        limit = len(operators)
        while count < limit:
            if operators[count] == "NOT":
                operators[count] = NOT(operators[count+1])
                operators.pop(count+1)
                limit-=1
            elif operators[count] in gates:
                if operators[count] == "AND": #,"OR","XOR","NAND"]
                operators[count-1],operators[count+1]

                
        
        



