# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def flatten(root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    # newRoot = TreeNode()
    # temp = newRoot
    # if root :
    #     newRoot.val = root.val
    #     newRoot.left = None
    #     newRoot.right = TreeNode()
    #     newRoot = newRoot.right

    #     root = root.right if root.left == None else root.left

    # root = temp
    def dfs(root):
        if not root:
            return None
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        last = rightTail or leftTail or root
        return last
    dfs(root)
