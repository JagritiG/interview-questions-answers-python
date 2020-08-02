# Binary Tree Preorder Traversa
# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?
# ======================================================================================
# Algorithm:
# iterative using stack, recursive
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=elQcrJrfObg
# ========================================================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1: iterative
def preorder_traversal_iter(root):

    if not root:
        return None

    result = []
    stack = [root]

    while stack:

        curr = stack.pop()
        result.append(curr.val)

        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)

    return result


# Method-2: recursive
def preorder_traversal_recur(root):
    """Left->Right->Root"""

    if not root:
        return []

    res = []

    def dfs(root):
        if root:

            # Then get the data of the node
            # print(str(root.val) + " ")
            res.append(root.val)

            # first perform recursion on left child
            dfs(root.left)

            # Then perform recursion on right child
            dfs(root.right)


    dfs(root)
    return res


if __name__ == "__main__":

    # Tree
    # root = [1,null,2,3]
    # L-1: root
    root = TreeNode(1)

    # L-2
    root.left = None
    root.right = TreeNode(2)

    # L-3
    # root.left.left = None
    # root.left.right = None
    root.right.left = TreeNode(3)
    root.right.right = None

    # # L-4
    # root.left.right.left = TreeNode(1)
    # root.left.right.right = None
    # root.right.right.left = TreeNode(6)
    # root.right.right.right = TreeNode(8)
    #
    # # L-5
    # root.left.right.left.left = None
    # root.left.right.left.right = None
    # root.right.right.left.left = None
    # root.right.right.left.right = None
    # root.right.right.right.left = TreeNode(1)
    # root.right.right.right.right = TreeNode(3)

    # print(root)
    print(preorder_traversal_iter(root))
    print(preorder_traversal_recur(root))

