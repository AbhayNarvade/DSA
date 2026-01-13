# 103. Binary Tree Zigzag Level Order Traversal

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Queue.Dynamic_circular_arry import DynamicQueue 
from Node import Node

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

arr =[]

def Level_order_traversal(root):
    if root is None :
        return 
    
    queue = DynamicQueue()
    queue.enqueue(root)
    arr.append(root.data)
    while queue.size > 0 :
        level = []
        
        for _ in range(queue.size):
            rootNode = queue.dequeue()
            if rootNode.left is not None:
                level.append(rootNode.left.data)
                queue.enqueue(rootNode.left)

            if rootNode.right is not None:
                level.append(rootNode.right.data)
                queue.enqueue(rootNode.right)
                    
        if len(level) > 0 :
            if len(arr) % 2 == 1 :
                level.reverse()
            arr.append(level)

    print(arr)

Level_order_traversal(root)
# output
# ['A', ['C', 'B'], ['D', 'E', 'F']]