class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BT:
    def __init__(self, root = None) -> None:
        self.root = root

    def insert(self, node, data):
        if (node == None):
            newnode = Node(data)
            print("Inserted ", newnode.data)
            return newnode
        else:
            choice = int(input("1. Left  2. Right: "))
            if choice == 1:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
        return node

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def height(self, node):
        if node == None:
            return 0
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return max(l_height, r_height)+1

bt = BT()

while True:
    choice = int(input("1. Insert 2. Preorder 3. Postorder 4. Inorder 5. Height 6. Exit\n"))
    if (choice == 1):
        data = int(input("Enter the value to be inserted: "))
        bt.root = bt.insert(bt.root, data)
    elif (choice == 2):
        bt.preorder(bt.root)
        print()
    elif (choice == 3):
        bt.postorder(bt.root)
        print()
    elif (choice == 4):
        bt.inorder(bt.root)
        print()
    elif (choice == 5):
        print(bt.height(bt.root))
    elif (choice == 6):
        break
