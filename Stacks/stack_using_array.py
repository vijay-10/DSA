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
        
    def display(self):
        if (self.top == -1):
            print("Stack Underflow")
        else:
            temp = self.top
            while(temp != -1):
                print("|",self.stack[temp],"|")
                print("-----")
                temp -= 1
            
    def peek(self):
        if (self.top == -1):
            print("Stack Underflow")
        else:
            print("Element at the top of stack: ", self.stack[self.top])

    def is_empty(self):
        if (self.top == -1):
            return True
        else:
            return False

stack = Stack(size=int(input("Enter the size of the stack: ")))

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
