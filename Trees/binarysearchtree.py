class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, root = None) -> None:
        self.root = root
        self.min_max = []

    def insert(self, node, data):
        if (node == None):
            newnode = Node(data)
            print("Inserted ", newnode.data)
            return newnode
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            elif data > node.data:
                node.right = self.insert(node.right, data)
            else:
                print("This value already exists in the tree.")
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
            self.min_max.append(node.data)
            print(node.data, end=" ")
            self.inorder(node.right)

    def search(self, node, key):
        if node != None:
            if (key == node.data):
                print(f"{key} found.")
            elif (key < node.data):
                self.search(node.left, key)
            elif (key > node.data):
                self.search(node.right, key)
        else:
            if self.root == None:
                print("Tree not found.")
            else:
                print(f"{key} not found.")

    def find_min_max(self, root):
        print("\nThe binary search tree is: ", end="")
        self.inorder(root)
        print("Minimum element is: ", self.min_max[0])
        print("Maximum element is: ", self.min_max[len(self.min_max)-1])
    
    def height(self, node):
        if node == None:
            return 0
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return max(l_height, r_height)+1



bst = BST()

while True:
    choice = int(input("1.Insert 2.Preorder 3.Postorder 4.Inorder 5.Search 6.Find Min & Max 7.Deletion 8.Height 9.Exit\n"))
    if (choice == 1):
        bst.root = bst.insert(bst.root, int(input("Enter the value to be inserted: ")))
    elif (choice == 2):
        bst.preorder(bst.root)
        print()
    elif (choice == 3):
        bst.postorder(bst.root)
        print()
    elif (choice == 4):
        bst.inorder(bst.root)
        print()
    elif (choice == 5):
        bst.search(bst.root, int(input("Enter the value to be searched: ")))
    elif (choice == 6):
        bst.find_min_max(bst.root)
    elif (choice == 8):
        print("Height of tree is: ", bst.height(bst.root))
    elif (choice == 9):
        break
