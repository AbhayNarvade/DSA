# 107. Binary Tree Level Order Traversal II

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
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue  = deque()
        queue.append(root)
        arr = []
        arr.append([root.val])

        while len(queue) > 0 :
            level = []
            for i in range(len(queue)):
                    
                popelement = queue.popleft()

                if popelement.left is not None :
                    level.append(popelement.left.val)
                    queue.append(popelement.left)

                if popelement.right is not None :
                    level.append(popelement.right.val)
                    queue.append(popelement.right)

            
            if len(level)>0 :
                arr.append(level)

        arr.reverse()
        return  arr
                



s = Solution()
print(s.levelOrderBottom(root))

# [[15, 7], [9, 20], [3]]