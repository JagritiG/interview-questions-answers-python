# Linked List in Binary Tree
# Given a binary tree root and a linked list with head as the first node.
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise return False.
# In this context downward path means a path that starts at some node and goes downwards.

# Example 1:
# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.

# Example 2:
# Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true

# Example 3:
# Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

# Constraints:
# 1 <= node.val <= 100 for each node in the linked list and binary tree.
# The given linked list will contain between 1 and 100 nodes.
# The given binary tree will contain between 1 and 2500 nodes.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description:  https://www.youtube.com/watch?v=92j3t--NkfI
# ========================================================================================
# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#         1
#       /   \
#     4      4 <-
#       \   /
#       2   2  <-
#     /    /  \
#    1    6    8 <-
#             / \
#            1   3


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def is_sub_path(head, root):

    def match(head, root):
        if not head:
            return True

        if not root or root.val != head.val:
            return False

        return match(head.next, root.left) or match(head.next, root.right)

    def dfs(head, root):
        if not root:
            return False

        if match(head, root):
            return True

        return dfs(head, root.left) or dfs(head, root.right)

    return dfs(head, root)


if __name__ == "__main__":

    # List
    node1 = SllNode(4)
    node1.next = SllNode(2)
    node1.next.next = SllNode(8)
    # node1.next.next.next = SllNode(5)
    # node1.next.next.next.next = SllNode(9)

    # Tree
    # root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    # L-1: root
    root = TreeNode(1)

    # L-2
    root.left = TreeNode(4)
    root.right = TreeNode(4)

    # L-3
    root.left.left = None
    root.left.right = TreeNode(2)
    root.right.left = None
    root.right.right = TreeNode(2)

    # L-4
    root.left.right.left = TreeNode(1)
    root.left.right.right = None
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(8)

    # L-5
    root.left.right.left.left = None
    root.left.right.left.right = None
    root.right.right.left.left = None
    root.right.right.left.right = None
    root.right.right.right.left = TreeNode(1)
    root.right.right.right.right = TreeNode(3)

    # print(root)
    print(is_sub_path(node1, root))
