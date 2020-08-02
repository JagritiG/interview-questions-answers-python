# Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Follow up: Solve it both recursively and iteratively.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=qNH6fFdb6Hs
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

    def is_mirror(leftchild, rightchild):

        if leftchild and rightchild:
            print(leftchild.val, rightchild.val)

            return leftchild.val == rightchild.val and \
                is_mirror(leftchild.left, rightchild.right) and \
                is_mirror(leftchild.right, rightchild.left)

        return leftchild == rightchild

    return is_mirror(root.left, root.right)


if __name__ == "__main__":

    # Tree
    # root = [1, 2, 2, 3, 4, 4, 3]
    #      1
    #     /  \
    #    2    2
    #   / \  / \
    #  3  4 4   3
    # root = [1, 2, 2, None, 3, None, 3]
    #        1
    #       / \
    #      2   2
    #      \    \
    #       3    3

    # L-1: root
    root = TreeNode(1)

    # L-2
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    # L-3
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # L-4
    root.left.left.left = TreeNode(5)
    root.left.left.right = TreeNode(6)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(2)
    root.right.left.right = TreeNode(3)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(5)

    # print(root)
    print(is_balanced(root))


