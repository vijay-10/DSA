class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert(self, val, index):
        if index==0:
            self.insert_first(val)
        elif index==self.size:
            self.insert_last(val)
        else:
            node = Node(val)
            ptr = self.get_node(index-1)
            node.next = ptr.next
            ptr.next = node
            self.size += 1

    def insert_last(self, val):
        node = Node(val)
        ptr = self.get_node(self.size-1)
        ptr.next = node
        self.size += 1

    def delete_first(self):
        self.head = self.head.next
        self.size -= 1

    def delete(self, index):
        if index == 0:
            self.delete_first()
        elif index == self.size-1:
            self.delete_last()
        else:
            ptr = self.get_node(index-1)
            ptr.next = ptr.next.next
            self.size -= 1

    def delete_last(self):
        ptr = self.get_node(self.size-2)
        ptr.next = None
        self.size -= 1

    def get_node(self, index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        return ptr

    def display(self):
        if (self.size==0):
            print("List empty")
            return
        ptr = self.head
        while(ptr!=None):
            print(f"{ptr.data}->", end='')
            ptr = ptr.next
        print("None")

list = SLL()

while True:
    print("""\nSingly Linked List MENU:\n\t1.Insert\n\t2.Delete\n\t3.Display\n\t4.Print Size\n\t5.Exit""")
    n = int(input("Enter yout choice: "))
    if (n==1):
        value = int(input("Enter the value to be inserted: "))
        position = int(input("Insert at:\n\t1.Beginning\n\t2.Middle\n\t3.End\n"))
        if position == 1:
            list.insert_first(value)
        elif position == 2:
            index = int(input("Enter the index at which the element needs to be inserted: "))
            list.insert(value, index)
        elif position == 3:
            list.insert_last(value)
    elif (n==2):
        position = int(input("Delete from:\n\t1.Beginning\n\t2.Middle\n\t3.End\n"))
        if position == 1:
            list.delete_first()
        elif position == 2:
            index = int(input("Enter the index at which the element needs to be deleted: "))
            list.delete(index)
        elif position == 3:
            list.delete_last()
    elif (n==3):
        list.display()
    elif (n==4):
        print(list.size)
    elif (n==5):
        break