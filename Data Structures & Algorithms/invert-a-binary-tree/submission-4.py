# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        templeft = root.left
        root.left = root.right
        root.right = templeft
        #inverse left sub-tree
        self.invertTree(root.left)
        #inverse right sub-tree
        self.invertTree(root.right)
        return root        


################ initial failed attempt
        # head = root
        # if head and root:
        #     while root.left:
        #         templeft = root.left
        #         tempright = root.right
        #         root.left = tempright
        #         root.right = templeft
        #         root = root.left
            
        #     root = head.right
        # if head and root:
        #     while root.right:
        #         templeft = root.left
        #         tempright = root.right
        #         root.left = tempright
        #         root.right = templeft
        #         root = root.right
        #     return head
        # return None