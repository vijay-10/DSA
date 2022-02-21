# Infix to Postfix using stack-array
class Stack:
    def __init__(self, size) -> None:
        self.top = -1
        self.size = size
        self.stack = [None]*size

    def push(self, val):
        if (self.top == self.size):
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = val
    
    def pop(self):
        if (self.top == -1):
            print("Stack Underflow")
        else:
            self.stack[self.top] = None
            self.top -= 1

    def is_empty(self):
        if (self.top == -1):
            return True
        else:
            return False

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
    stack = Stack(len(infix_exp)//2+1)
    
    for i in infix_exp:
        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            postfix_exp += i
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not(stack.is_empty()) and stack.stack[stack.top] != "(":
                postfix_exp += stack.stack[stack.top]
                stack.pop()
            if not(stack.is_empty()):
                stack.pop()
        else:
            while not(stack.is_empty()) and precedence(stack.stack[stack.top]) > precedence(i):
                postfix_exp += stack.stack[stack.top]
                stack.pop()
            stack.push(i)

    while not(stack.is_empty()):
        postfix_exp += stack.stack[stack.top]
        stack.pop()

    return postfix_exp

exp = infix_to_postfix("(a-b/c)*(a/k-l)")
print(exp)