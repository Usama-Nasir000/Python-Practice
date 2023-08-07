
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_Child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_Child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_Child(data)
            else:
                self.right = TreeNode(data)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        
        if node is None:
            return TreeNode(data)
        
       
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        
        return node
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(0)
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(2)
bst.insert(3)
bst.insert(3)

print("Inorder traversal:", bst.inorder_traversal())

search_key = 8
search_result = bst.search(search_key)
if search_result:
    print(f"Key {search_key} found in the tree.")
else:
    print(f"Key {search_key} not found in the tree.")


# AVL Tree
class AVLNode(TreeNode):
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree(BinarySearchTree):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, root, data):
        if root is None:
            return AVLNode(data)
        
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        if balance > 1:
            if data < root.left.data:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < -1:
            if data > root.right.data:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_data(self, data):
        self.root = self.insert(self.root, data)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

avl_tree = AVLTree()

data_list = [1,6,8,11,25,9,16,20]

for data in data_list:
    avl_tree.insert_data(data)

print("Preorder traversal of AVL tree:")
avl_tree.preorder_traversal(avl_tree.root)