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
    for x in range(2):
        expression += "(" + generate_subexpression() + ")"
        if x < 1:
            expression += random.choice(gates)
    return expression

def solve(expression):
    temp = re.sub(r'\(+|\)+', ' ', expression)
    operators = list(temp.split(" "))
    operators.pop(0)
    operators.pop(-1)

    answers = []
    values = [[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]]

    for x in range(len(values)):
        operators2 = list(operators)
        for y in range(len(operators)):
            if operators[y] == "A":
                operators2[y] = values[x][0]
            elif operators[y] == "B":
                operators2[y] = values[x][1]
            elif operators[y] == "C":
                operators2[y] = values[x][2]

        count = 0

        while "NOT" in operators2:
            if operators2[count] == "NOT":
                operators2[count] = NOT(operators2[count+1])
                operators2.pop(count+1)
            count+=1

        count = 0

        for y in range(2):
            if y == 0:
                count = 1
            else:
                count = 3
            if operators2[count] == "AND": 
                operators2[count] = AND(operators2[count-1],operators2[count+1])
            elif operators2[count] == "OR": 
                operators2[count] = OR(operators2[count-1],operators2[count+1])
            elif operators2[count] == "XOR": 
                operators2[count] = XOR(operators2[count-1],operators2[count+1])
            else:
                operators2[count] = NAND(operators2[count-1],operators2[count+1])
            operators2.pop(count-1)
            operators2.pop(count)

        if operators2[1] == "AND": 
            answers.append(AND(operators2[0],operators2[2]))
        elif operators2[1] == "OR": 
            answers.append(OR(operators2[0],operators2[2]))
        elif operators2[1] == "XOR": 
            answers.append(XOR(operators2[0],operators2[2]))
        else:
            answers.append(NAND(operators2[0],operators2[2]))
                
    return answers
        
def check(m):
    outlist = []
    for x in range(8):
        temp = int(input())
        if temp == m[x]:
            outlist.append('right')
        else:
            outlist.append('wrong')
    print(m)
    return outlist

def high_score(n):
    try:
        with open("high_score.txt", "r") as file:
            hscore = int(file.read())
            if n > hscore:
                file = open("high_score.txt", "w")
                file.write(str(n))
                file.close()
                return 1
            else:
                file.close()
                return 1
    except FileNotFoundError:
        file = open("high_score", "w")
        file.write(str(n))
        file.close()
        return 1

count = 0
while True:
    expression = generate_expression()

    print("Complete the tracetable for X="+expression+".")
    print("|  A  |  B  |  C  |  X  |")
    print("|-----------------------|")
    print("|  1  |  1  |  1  |     |")
    print("|  1  |  1  |  0  |     |")
    print("|  1  |  0  |  1  |     |")
    print("|  1  |  0  |  0  |     |")
    print("|  0  |  1  |  1  |     |")
    print("|  0  |  1  |  0  |     |")
    print("|  0  |  0  |  1  |     |")
    print("|  0  |  0  |  0  |     |")

    answer = solve(expression)
    temp = check(answer)
    print(temp)
    if temp.count('right') == 8:
        count += 1
    high_score(count)
