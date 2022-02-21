class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
class AVL:
    def __init__(self) -> None:
        self.root = None

    def insert(self, node, data):
        if (node == None):
            return  Node(data)
 
        if (data < node.data):
            node.left  = self.insert(node.left, data)
        elif (data > node.data):
            node.right = self.insert(node.right, data)
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance_factor(node)

        # LL
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)
        
        # RR
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        # LR
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)        

        return node

    def balance_factor(self, node):
        if node == None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def height(self, node):
        if node == None:
            return 0
        return node.height

    def left_rotate(self, node):
        new = node.right
        temp = new.left
        new.left = node
        node.right = temp

        new.height = 1 + max(self.height(new.left), self.height(new.right))
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return new

    def right_rotate(self, node):
        new = node.left
        temp = new.right
        new.right = node
        node.left = temp

        new.height = 1 + max(self.height(new.left), self.height(new.right))
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return new

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


avl = AVL()
avl.root = avl.insert(avl.root, 1)
avl.root = avl.insert(avl.root, 2)
avl.root = avl.insert(avl.root, 4)
avl.root = avl.insert(avl.root, 5)
avl.root = avl.insert(avl.root, 6)
avl.root = avl.insert(avl.root, 3)
avl.preorder(avl.root)