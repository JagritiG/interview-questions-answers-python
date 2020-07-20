# Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.

# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
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


def remove_elements(head, val):

    # Input: 1->2->6->3->4->5->6 Null
    # val = 6
    # Output: 1->2->3->4->5-> Null

    if not head:
        return head

    curr = head
    prev = None

    while curr:

        if curr == head and curr.val == val:
            head = head.next
            curr = head

        elif curr != head and curr.val == val:
            prev.next = curr.next
            curr = curr.next

        else:
            prev = curr
            curr = curr.next

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
    node1.next.next = SllNode(6)
    node1.next.next.next = SllNode(3)
    node1.next.next.next.next = SllNode(4)
    node1.next.next.next.next.next = SllNode(5)
    node1.next.next.next.next.next.next = SllNode(6)
    data = 6

    print(remove_elements(node1, data))
