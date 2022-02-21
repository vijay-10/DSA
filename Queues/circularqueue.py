class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.cq=[None]*size
        self.front=-1
        self.rear=-1

    def insert(self):
        data=int(input("Enter value to be inserted: "))
        if (self.front==(self.rear+1)%self.size):
            print("Overflow")
        elif (self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0    
        else:
            self.rear=(self.rear+1)%self.size
            self.cq[self.rear]=data
    
    def delete(self):
        if self.rear==-1:
            print("Underflow")
        else:
            if (self.front==self.rear):
                self.front=-1
                self.rear=-1
            elif (self.front==self.size-1):
                self.front=0
            else:
                self.front=(self.front+1)%self.size

    def display(self):
        if self.rear==-1:
            print("Queue is empty")
        if self.front>=self.rear:
            for x in range(self.front,self.size):
                print(self.cq[x],end=' ')
            for x in range(0,self.rear+1):
                print(self.cq[x],end=' ')
        else:
            for x in range(self.front,self.rear+1):
                print(self.cq[x],end=" ")
            print("\n")

n=int(input("Enter size of the Queue: "))
cq=CircularQueue(n)
while True:
    choice=int(input("\n1. Enqueue\t2. Dequeue\t3. Display\t4. Exit\nEnter your choice: "))
    if choice==1:
        cq.insert()
    elif choice==2:
        cq.delete()
    elif choice==3:
        cq.display()
    elif choice==4:
        break
    else:
        print("Wrong choice, try again")