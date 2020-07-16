# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
def merge_two_lists(l1, l2):

    new_list = SllNode()
    curr = new_list

    if not l1:
        return l2
    if not l2:
        return l1

    # Traverse two lists, compare, and merge them
    while l1 and l2:

        if l1.val <= l2.val:
            curr.next = l1
            curr = l1
            l1 = curr.next

        else:
            curr.next = l2
            curr = l2
            l2 = curr.next

        if not l1:
            curr.next = l2

        if not l2:
            curr.next = l1

    def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next

    # print([new_list, new_list.next, new_list.next.next, new_list.next.next.next])
    print_list(new_list.next)
    return new_list.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(4)

    node2 = SllNode(1)
    node2.next = SllNode(3)
    node2.next.next = SllNode(4)
    print("Input Lists:")
    print([node1, node1.next, node1.next.next])
    print([node2, node2.next, node2.next.next])
    print("\n")
    print("Output:")
    print(merge_two_lists(node1, node2))




