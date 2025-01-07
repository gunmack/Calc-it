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

def precedence_of(op):
    return precedence[op] if op in precedence else 0

def tokenize(expression):
    # Tokenize numbers and operators
    tokens = re.findall(r'\d+\.\d+|\d+|[-+/*()]', expression)

    
    if tokens[0] == '-':
        tokens[1] = '-' + tokens[1]
        tokens.pop(0)
    
    if tokens[0] == '+':
        tokens.pop(0)
  
    i = 1  # Start from the second token
    while i < len(tokens):  # Use a while loop for more control
        if tokens[i] == '-' and tokens[i+1] in {'+', '-'}: 
            tokens[i+1] = '-' + tokens[i+1]
            tokens.pop(i+1)
            continue  # Restart at the same index after modifying

        if tokens[i] == '+' and tokens[i+1] in {'+', '-'}:
            tokens.pop(i)
            continue  # Restart at the same index after modifying

        if tokens[i] in {'+', '-'} and (tokens[i-1] in {'(', '+', '-'}):
            tokens[i+1] = tokens[i] + tokens[i+1]
            tokens.pop(i)
            continue  # Restart at the same index after modifying

        i += 1  # Move to the next token only if no modifications

    print(tokens)
    return tokens

def evaluate_expression(expression):
    tokens = tokenize(expression)
    values = []  # Stack for numbers
    operators = []  # Stack for operators

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # If token is a number (including negative numbers), push to values stack
        if re.match(r'-?\d+\.?\d*', token):
            if '.' in token:
                values.append(float(token))  # Float number
            else:
                values.append(int(token))  # Integer number

        # If token is '(', push to operators stack
        elif token == '(':
            operators.append(token)

        # If token is ')', pop and apply operators until '('
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Pop the '('

        # If token is an operator, apply operators while precedence allows
        elif token in precedence:
            while (operators and operators[-1] != '(' and precedence_of(operators[-1]) >= precedence_of(token)):
                apply_operator(operators, values)
            operators.append(token)

        i += 1

    # Apply remaining operators
    while operators:
        apply_operator(operators, values)

    return values[0]
