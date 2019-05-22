# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBSTRecurs(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        if root.val >= L and root.val <= R:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        elif root.val <= L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val >= R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return 0
    
    def rangeSumBSTIter(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        stack = [root]
        while len(stack) > 0:
            val = stack.pop()
            if val == None:
                continue
            if val.val >= L and val.val <= R:
                sum += val.val
                stack.append(val.left)
                stack.append(val.right)
            elif val.val <= L:
                stack.append(val.right)
            elif val.val >= R:
                stack.append(val.left)
        return sum