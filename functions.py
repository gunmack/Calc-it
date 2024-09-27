import re

def add(x,y):
    if ((type(x)==float) or (type(y)==float)):
        return float(x)+float(y)
    else:
        res = float(x)+float(y)
        return(int(res))

def subtract(x,y):
    if ((type(x)==float) or (type(y)==float)):
        return float(x)-float(y)
    else:
        return int(float(x)-float(y))

def multiply(x,y):
    if ((type(x)==float or type(y)==float)):
        a = float(x)
        b = float(y)
        return float(a*b)
    else:
        return int(float(x)*float(y))

def divide(x,y):
    if ((type(x)==float) or (type(y)==float)):
        a = float(x)
        b = float(y)
        return float(a/b)
    else:
        return (x)/(y)

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def tokenize(expression):
   
    tokens = re.findall(r'\d+\.\d+|\d+|[-+/*()]', expression)
    if len(tokens)>1 and tokens[0] == '-':
        tokens[1] = '-' + tokens[1]
        tokens.pop(0)
 
    for i in range(2,len(tokens)):
        if ((tokens[i] == '-') or (tokens[i] == '+'))  and tokens[i+1].isdigit() and tokens[i-1] == '(':
               
            if tokens[i] == '-': 
                tokens[i+1] = '-' + tokens[i+1]
                tokens.pop(i)
            if tokens[i] == '+':
                tokens.pop(i)
            break
    return tokens

def evaluate_expression(expression):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        
        if operator == '+':
            values.append(add(left,right))
            
        elif operator == '-':
            values.append(subtract(left,right))
        
        elif operator == '*':
            values.append(multiply(left,right))
           
        elif operator == '/':
            values.append(divide((left),(right)))
    
    def precedence(op):
        return precedence[op] if op in precedence else 0

    
    tokens = tokenize(expression)
    values = []
    operators = []
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isdigit() or re.match(r'-?\d+\.?\d*', token):
            if '.' in token:
                values.append(float(token))
            else:
                values.append(int(token))

        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            while (operators and precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)
        
        i += 1
    while operators:
        apply_operator(operators, values)
    
    return values[0]
