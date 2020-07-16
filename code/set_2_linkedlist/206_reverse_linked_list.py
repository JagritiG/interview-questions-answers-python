# Reverse Linked List
# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
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


# method-1: recursive
def reverse_list_recursive(head):
    """Reverse a linked list using recursion."""

    def helper(curr, prev):

        if not curr:
            return prev

        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        return helper(curr, prev)

    head = helper(head, None)
    return head


# method-2: iterative
def reverse_list_iterative(head):
    """Reverse a linked list iteratively."""

    # 1 -> 2 -> 3 -> 4 -> 5 -> Null
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev

    def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next

    # print([new_list, new_list.next, new_list.next.next, new_list.next.next.next])
    print_list(head)
    return head


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)

    # print("Input Lists:")
    # print([node1, node1.next, node1.next.next])
    # print("\n")
    print("Output:")
    print(reverse_list_recursive(node1))
    # print(reverse_list_iterative(node1))
