# Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
# ======================================================================================
# Algorithm:
# iterative using stack, recursive
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=nzmtCFNae9k,
# https://www.youtube.com/watch?v=gm8DUJJhmY4
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
def inorder_traversal_iter(root):

    if not root:
        return None

    res = []
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left

        else:
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                break

    return res


# Method-2: recursive
def inorder_traversal_recur(root):
    """Left->Root->Right"""

    if root:

        # first perform recursion on left child
        inorder_traversal_recur(root.left)

        # Then get the data of the node
        print(str(root.val) + " ")

        # Then perform recursion on right child
        inorder_traversal_recur(root.right)


# # Method-3: Morris inorder traversal
# https://www.youtube.com/watch?v=wGXB9OWhPTg


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
    print(inorder_traversal_iter(root))
    inorder_traversal_recur(root)

