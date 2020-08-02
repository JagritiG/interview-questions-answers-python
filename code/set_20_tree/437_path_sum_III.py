# Path Sum III
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC:
# Description:
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
    count = 0

    def find_path(root, sum, curr, result, count):

        if not root:
            return

        curr.append(root.val)
        if root.val == sum:
            result.append(curr)
            count += 1
            return

        find_path(root.left, sum - root.val, curr.copy(), result, count)
        find_path(root.right, sum - root.val, curr.copy(), result, count)

    find_path(root, sum, [], result, count)
    print(result)
    return count


if __name__ == "__main__":

    # Tree
    # root = [10,5,-3,3,2,null,11,3,-2,null,1]
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1

    # L-1: root
    root = TreeNode(10)

    # L-2
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    # L-3
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.left = None
    root.right.right = TreeNode(11)

    # # L-4
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.left = None
    root.left.right.right = TreeNode(1)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)


    # # L-5
    # root.left.right.left.left = None
    # root.left.right.left.right = None
    # root.right.right.left.left = None
    # root.right.right.left.right = None
    # root.right.right.right.left = TreeNode(1)
    # root.right.right.right.right = TreeNode(3)

    s = 8
    # print(root)
    print(has_path_sum(root, s))

