def precedence(op):
        if op == '^':
            return 3
        elif op == "/" or op == "*" or op == "%":
            return 2
        elif op == "+" or op == "-":
            return 1
        else:
            return -1

def infix_to_postfix(infix_exp):
    postfix_exp = ""
    stack = []
    
    for i in infix_exp:
        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            postfix_exp += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while not(len(stack)==0) and stack[-1] != "(":
                postfix_exp += stack[-1]
                stack.pop()
            if not(len(stack)==0):
                stack.pop()
        else:
            while not(len(stack)==0) and precedence(stack[-1]) > precedence(i):
                postfix_exp += stack[-1]
                stack.pop()
            stack.append(i)

    while not(len(stack)==0):
        postfix_exp += stack[-1]
        stack.pop()

    return postfix_exp

print(infix_to_postfix("(a-b/c)*(a/k-l)"))