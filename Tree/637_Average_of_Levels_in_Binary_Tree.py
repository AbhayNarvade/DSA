# 637. Average of Levels in Binary Tree

# Node class definition
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create the tree:
#       3
#      / \
#     9  20
#        / \
#       15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []

        queue = deque([root])
        arr = []

        while queue:
            total = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            arr.append(total / float(level_count)) 

        return arr
    

s = Solution()
print(s.averageOfLevels(root)) 
# [3.0, 14.5, 11.0]