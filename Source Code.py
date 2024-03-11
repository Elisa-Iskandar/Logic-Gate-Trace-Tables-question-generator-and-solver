import random
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

print(generate_expression())
