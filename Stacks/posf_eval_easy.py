def postfix_evaluation(postfix_exp):
    stack = []
    for i in postfix_exp:
        if i>='0' and i<='9':
            stack.append(int(i))
        else:
            op2 = stack[-1]
            stack.pop()
            op1 = stack[-1]
            stack.pop()

            if i == "+":
                stack.append(op1+op2)
            elif i == "-":
                stack.append(op1-op2)
            elif i == "*":
                stack.append(op1*op2)
            elif i == "/":
                stack.append(op1/op2)
            elif i == "%":
                stack.append(op1%op2)
            elif i == "^":
                stack.append(op1**op2)
            
    return stack[-1]

print(postfix_evaluation("46+2/5*7+"))
