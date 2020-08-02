# Path Sum II
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.

# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC:
# Description: https://www.youtube.com/watch?v=3B5gnrwRmOA
# ========================================================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1:
def has_path_sum(root, sum):

    result = []

    def find_path(root, sum, curr, result):

        if not root:
            return

        curr.append(root.val)
        # check if current node is a leaf node or not
        if not root.left and not root.right and root.val == sum:
                result.append(curr)
                return

        find_path(root.left, sum - root.val, curr.copy(), result)
        find_path(root.right, sum - root.val, curr.copy(), result)

    find_path(root, sum, [], result)
    return result


if __name__ == "__main__":

    # Tree
    # root = [5, 4, 8, 11, Null, 13, 4, 7, 2, 5, 1]
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \    / \
    # 7    2  5   1

    # L-1: root
    root = TreeNode(5)

    # L-2
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    # L-3
    root.left.left = TreeNode(11)
    root.left.right = None
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    # # L-4
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left.left = None
    root.right.left.right = None
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)


    # # L-5
    # root.left.right.left.left = None
    # root.left.right.left.right = None
    # root.right.right.left.left = None
    # root.right.right.left.right = None
    # root.right.right.right.left = TreeNode(1)
    # root.right.right.right.right = TreeNode(3)

    s = 22
    # print(root)
    print(has_path_sum(root, s))


