# Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.

# Follow up:
# Could you do this in one pass?
# ======================================================================================
# Algorithm:
# TC:
# SC:
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# method-1
def remove_Nth_from_end(head, n):

    curr = head

    # Size of the list
    size = 0
    while curr:
        size += 1
        curr = curr.next

    # When given position is greater than size of list
    if n > size:
        return None

    # When list is empty
    if not head:
        return None

    # Delete first node
    elif n == size:
        curr = head
        temp = curr.next
        head = temp

    # Delete last node
    elif n == 1:
        curr = head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        curr = prev
        curr.next = None

    # Delete nth node from end
    else:
        curr = head
        prev = None
        curr_position = 0
        while curr_position < size-n and curr.next:
            prev = curr
            curr = curr.next
            curr_position += 1

        prev.next = curr.next

    # print([head, head.next, head.next.next, head.next.next.next])
    return head


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)
    n = 2


    print("Input Lists:")
    # print([node1, node1.next, node1.next.next, node1.next.next.next, node1.next.next.next.next])
    print("\n")
    print("Output:")
    print(remove_Nth_from_end(node1, n))




