# Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=_pP1UaL-Xi8
# ========================================================================================
import collections


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1: recursive
# Tc: O(n)
# Sc: O(n)
def is_balanced(root):

    if not root:
        return True

    def get_height(node):

        if not node:
            return 0

        left = get_height(node.left)
        right = get_height(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return get_height(root) != -1


if __name__ == "__main__":

    # Tree
    # root = [3, 9, 20, None, None, 15, 7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = [1, 2, 2, 3, 3, None, None, 4, 4]
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4

    # L-1: root
    root = TreeNode(1)

    # L-2
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    # L-3
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = None
    root.right.right = None

    # L-4
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    # print(root)
    print(is_balanced(root))

