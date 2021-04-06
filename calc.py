import math as m


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    return False


def pre(n):
    if n == '+' or n == '-':
        return 1
    elif n == '*' or n == '/':
        return 2
    elif n == '^':
        return 3


def assoc(n):
    if n == '^':
        return 'right'
    else:
        return 'left'


def onp(n):
    norm = n.split()

    output = []
    stack = []

    for j in norm:
        if is_number(j):
            output.append(float(j))
        elif j == 'sin' or j == 'cos':
            stack.append(j)
        elif j == '+' or j == '-' or j == '*' or j == '/' or j == '^':
            while len(stack) > 0 and stack[-1] != '(' and (
                    pre(stack[-1]) > pre(j) or (pre(stack[-1]) == pre(j) and assoc(j) == 'left')):
                output.append(stack.pop())
            stack.append(j)
        elif j == '(':
            stack.append(j)
        elif j == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            if stack[-1] == '(':
                stack.pop()
            if len(stack) > 0 and (stack[-1] == 'sin' or stack[-1] == 'cos'):
                output.append(stack.pop())

    while len(stack) > 0:
        output.append(stack.pop())

    return output


while True:
    d = input('> ')

    if d == 'exit' or d == 'quit' or d == 'wyjście' or d == 'koniec':  # przerwanie programu
        break

    notacja = onp(d)  # zamiana normalnej notacji na ONP

    # obliczanie wartości:

    stos = []

    for i in notacja:
        if isinstance(i, float):
            stos.append(i)
        else:
            a = stos.pop()
            b = stos.pop()
            if i == '+':
                stos.append(b + a)
            elif i == '-':
                stos.append(b - a)
            elif i == '*':
                stos.append(b * a)
            elif i == '/':
                stos.append(b / a)
            elif i == '^':
                stos.append(b ** a)
            elif i == 'sin':
                stos.append(m.sin(a))
            elif i == 'cos':
                stos.append(m.cos(a))

    print(stos[0])
