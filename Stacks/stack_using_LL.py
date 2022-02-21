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
    
    def peek(self):
        if self.top == None:
            print("Stack empty")
        else:
            print(self.top.data)
    
    def display(self):
        if self.top == None:
            print("Stack empty")
        else:
            ptr = self.top
            while(ptr!=None):
                print(ptr.data)
                ptr = ptr.next

stack = Stack()        
while True:
    print("\n\t1.Push\n\t2.Pop\n\t3.Display\n\t4.Peek\n\t5.Is Empty\n\t6.Exit")
    choice = int(input("Enter the operation you want to perform: "))
    if (choice == 1):
        val = int(input("Enter the value to be pushed: "))
        stack.push(val)
    elif (choice == 2):
        stack.pop() 
    elif (choice == 3): 
        stack.display()
    elif (choice == 4): 
        stack.peek()
    elif (choice == 5):
        print(stack.is_empty())
    elif (choice == 6):
        break
    else:
        print("Invalid operation")
