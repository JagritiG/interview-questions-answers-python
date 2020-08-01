# Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=z2LEbk5l_gg
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
def min_depth(root):

    if not root:
        return 0

    q = collections.deque()
    q.append(root)
    depth = 0

    while q:
        size = len(q)

        while size > 0:
            curr = q.popleft()

            if not curr.left and not curr.right:
                depth += 1
                return depth

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

            size -= 1

        depth += 1


if __name__ == "__main__":

    # Tree
    root = [3, 9, 20, None, None, 15, 7]
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
    print(min_depth(root))

