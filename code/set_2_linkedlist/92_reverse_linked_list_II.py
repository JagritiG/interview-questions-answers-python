# Reverse Linked List II
# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=BE0hruM5O5U
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# method-2: iterative
def reverse_between(head, start, end):
    """Reverse a linked list from m to n node."""

    # 1 -> 2 -> 3 -> 4 -> 5 -> Null
    # m = 2, n = 4
    # 1 -> 4 -> 3 -> 2 -> 5 -> Null

    if not head or start == end:
        return head

    rev_list = SllNode(0)
    rev_list.next = head
    node_before_sublist = rev_list
    position = 1
    while position < start:
        node_before_sublist = node_before_sublist.next
        position += 1
    # print(node_before_sublist, position)

    curr = node_before_sublist.next
    while start < end:
        node_tobe_reversed = curr.next
        curr.next = node_tobe_reversed.next
        node_tobe_reversed.next = node_before_sublist.next
        node_before_sublist.next = node_tobe_reversed
        start += 1

    # print(position)

    def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next

    # print([new_list, new_list.next, new_list.next.next, new_list.next.next.next])
    print_list(head)
    return rev_list.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)
    m = 2
    n = 4

    # print("Input Lists:")
    # print([node1, node1.next, node1.next.next])
    # print("\n")
    print("Output:")
    # print(reverse_list_recursive(node1))
    print(reverse_between(node1, m, n))
