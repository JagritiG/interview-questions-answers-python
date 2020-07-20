# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.
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


def swap_pairs(head):

    # Input: 1->2->3->4
    # Output: 2->1->4->3

    if not head or not head.next:
        return head

    curr = head
    while curr and curr.next:

        curr.val, curr.next.val = curr.next.val, curr.val
        curr = curr.next.next

    print_list(head)
    return head


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)

    print(swap_pairs(node1))
