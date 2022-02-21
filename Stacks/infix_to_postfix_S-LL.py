# Infix to Postfix using stack-linkedlist
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top == None:
            print("Stack underflow")
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped
    
    def is_empty(self):
        if self.top == None:
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
    stack = Stack()
    for i in infix_exp:
        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            postfix_exp += i
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not(stack.is_empty()) and stack.top.data != "(":
                postfix_exp += stack.top.data
                stack.pop()
            if not(stack.is_empty()):
                stack.pop()
        else:
            while not(stack.is_empty()) and precedence(stack.top.data) > precedence(i):
                postfix_exp += stack.top.data
                stack.pop()
            stack.push(i)

    while not(stack.is_empty()):
        postfix_exp += stack.top.data
        stack.pop()

    return postfix_exp

print(infix_to_postfix("(a-b/c)*(a/k-l)"))