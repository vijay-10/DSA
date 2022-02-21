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

def postfix_evaluation(postfix_exp):
    stack = Stack()
    for i in postfix_exp:
        if i>='0' and i<='9':
            stack.push(int(i))
            # stack.push((i))
        else:
            op2 = stack.top.data
            stack.pop()
            op1 = stack.top.data
            stack.pop()

            if i == "+":
                stack.push(op1+op2)
            elif i == "-":
                stack.push(op1-op2)
            elif i == "*":
                stack.push(op1*op2)
            elif i == "/":
                stack.push(op1/op2)
            elif i == "%":
                stack.push(op1%op2)
            elif i == "^":
                stack.push(op1**op2)
            
    return stack.top.data

print(postfix_evaluation("46+2/5*7+"))
# print(postfix_evaluation("abc/-ak/l-*"))
