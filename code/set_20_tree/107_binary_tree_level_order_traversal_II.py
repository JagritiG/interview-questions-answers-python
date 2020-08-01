# Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# ======================================================================================
# Algorithm:
# iterative using queue
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=H2K0CGAjQDc
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


# breadth-first-traversal
# Method-1: iterative using queue
# Tc: O(n)
# Sc: O(n)
def levelorder_bottom_iter(root):

    if not root:
        return []

    # res = collections.deque()
    res = []
    q = collections.deque()
    q.append(root)

    while q:

        size = len(q)
        level = []

        while size > 0:
            curr_node = q.popleft()

            if curr_node.left:
                q.append(curr_node.left)

            if curr_node.right:
                q.append(curr_node.right)

            level.append(curr_node.val)
            size -= 1

        res.insert(0, level)

    return res


# breadth-first-traversal
# Method-1: recursive
# Tc: O(n)
# Sc: O(n)
def levelorder_bottom_recur(root):

    result = []

    def dfs(node, level, result):
        if node:
            if level >= len(result):
                result.insert(0, [])
            result[-(level+1)].append(node.val)
            dfs(node.left, level+1, result)
            dfs(node.right, level+1, result)

    dfs(root, 0, result)
    return result


if __name__ == "__main__":

    # Tree
    root = [3,9,20,None,None,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    # L-1: root
    root = TreeNode(3)

    # # L-2
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    # # L-3
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # print(root)
    print(levelorder_bottom_iter(root))
    print(levelorder_bottom_recur(root))




