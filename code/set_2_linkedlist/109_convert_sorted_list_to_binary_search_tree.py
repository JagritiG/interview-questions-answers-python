# Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
# subtrees of every node never differ by more than 1.

# Example:
# Given the sorted linked list: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description:
# ========================================================================================


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
def sorted_list_to_bst(head):

    # LL: [-10,-3,0,5,9]
    def create_bst(head, tail):

        if head == tail:
            return None

        slow = fast = head
        # Find mid of list
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next

        # Create Root, left child, right child of BST
        root = TreeNode(slow.val)
        root.left = create_bst(head, slow)
        root.right = create_bst(slow.next, tail)
        return root

    curr = head
    tail = None
    return create_bst(curr, tail)


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(-10)
    node1.next = SllNode(-3)
    node1.next.next = SllNode(0)
    node1.next.next.next = SllNode(5)
    node1.next.next.next.next = SllNode(9)

    print(sorted_list_to_bst(node1))
