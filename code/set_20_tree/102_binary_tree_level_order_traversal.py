# Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# ======================================================================================
# Algorithm:
# iterative using queue
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=9PHkM0Jri_4,
# https://www.youtube.com/watch?v=clQmmlCTy7E
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
def levelorder_traversal_iter(root):

    if not root:
        return []

    res = []
    q = collections.deque([root])


    while q:

        level = []

        for _ in range(len(q)):

            curr = q.popleft()
            level.append(curr.val)

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        res.append(level)

    return res


# breadth-first-traversal
# Method-1: recursive
# Tc: O(n)
# Sc: O(n)
def levelorder_traversal_recur(root):

    if not root:
        return []

    # res = collections.defaultdict(list)
    res = dict()

    def helper(node, level):
        # res[level].append(node.val)
        if level not in res:
            res[level] = [node.val]
        else:
            res[level].append(node.val)

        if node.left:
            helper(node.left, level+1)
        if node.right:
            helper(node.right, level+1)

    helper(root, 0)
    return res.values()


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
    print(levelorder_traversal_iter(root))
    print(levelorder_traversal_recur(root))



