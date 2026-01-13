from Node import Node

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F  


root = Node('A')

root.left = Node('B')
root.right = Node('C')

root.left.left = Node('D')
root.left.right = Node('E')

root.right.right = Node('F')

# -------- Preorder --------
pre = []
def preorder(root):
    if root is None:
        return 
    
    pre.append(root.data)
    preorder(root.left)
    preorder(root.right)

preorder(root)

# -------- Postorder --------
post = []
def postorder(root):
    if root is None:
        return 
    
    postorder(root.left)
    postorder(root.right)
    post.append(root.data)

postorder(root)

# -------- Inorder --------
In = []

def Inorder(root):
    if root is None:
        return 
    
    Inorder(root.left)
    In.append(root.data)
    Inorder(root.right)


Inorder(root)

print(pre)  # ['A', 'B', 'D', 'E', 'C', 'F']
print(In)   # ['D', 'B', 'E', 'A', 'C', 'F']
print(post) # ['D', 'E', 'B', 'F', 'C', 'A']



