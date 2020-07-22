# Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# ======================================================================================
# Algorithm:
# 1. Separate the list in two parts at the middle:
# 2. Reverse the second half
# 3. Merge two separated list
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=xRYPjDMSUFw
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def reorder_list(head):

    # Input: 1->2->3->4->5
    # Output: 1->5->2->4->3

    if not head or not head.next:
        return

    def reverse_list(head):
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def merge_lists(l1, l2):
        while l1:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2

            if l1_next is None:
                break

            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next

    # Separate the list in two parts at the middle
    l1 = head
    slow = head
    fast = head

    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None    # tail of first linked list

    # Reverse the second half
    l2 = reverse_list(slow)   # slow: head of second list

    # Merge two separated lists
    merge_lists(l1, l2)

    print_list(l1)
    return l1


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
    node1.next.next.next.next = SllNode(5)

    print(reorder_list(node1))

