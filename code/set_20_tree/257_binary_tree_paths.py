# Binary Tree Paths
# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.

# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC:
# Description: https://www.youtube.com/watch?v=zIkDfgFAg60
# ========================================================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1: recursive
def binary_tree_paths(root):

    result = []
    if not root:
        return result

    def dfs(root, curr_path, result):

        curr_path += str(root.val)
        if not root.left and not root.right:
            result.append(curr_path)
            return

        if root.left:
            dfs(root.left, curr_path + "->", result)

        if root.right:
            dfs(root.right, curr_path + "->", result)

    dfs(root, "", result)
    return result


if __name__ == "__main__":

    # Tree
    # root = [1, 2, 3, Null, 5]
    #    1
    #  /   \
    # 2     3
    #  \
    #   5
    # L-1: root
    root = TreeNode(1)

    # L-2
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # L-3
    root.left.left = None
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)

    # # L-4
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.left.left = None
    # root.right.left.right = None
    # root.right.right.left = None
    # root.right.right.right = TreeNode(1)


    # # L-5
    # root.left.right.left.left = None
    # root.left.right.left.right = None
    # root.right.right.left.left = None
    # root.right.right.left.right = None
    # root.right.right.right.left = TreeNode(1)
    # root.right.right.right.right = TreeNode(3)

    # print(root)
    print(binary_tree_paths(root))
