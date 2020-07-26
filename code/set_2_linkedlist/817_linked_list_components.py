# Linked List Components
# We are given head, the head node of a linked list containing unique integer values.
# We are also given the list G, a subset of the values in the linked list.

# Return the number of connected components in G, where two values are connected if
# they appear consecutively in the linked list.

# Example 1:
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

# Example 2:
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

# Note:
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N - 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=uFso48YRRao,
# https://www.youtube.com/watch?v=wVsGnpXoxPI
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def num_components(head, g):

    # Input:
    # head: 0->1->2->3->4
    # G = [0, 3, 1, 4]
    # Output: 2:  (0-1, 3-4)

    count = 0               # number of connected components

    curr = head
    while curr:
        if curr.val in g:
            count += 1
            while curr and curr.val in g:
                curr = curr.next

        else:
            curr = curr.next

    return count


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":

    node1 = SllNode(0)
    node1.next = SllNode(1)
    node1.next.next = SllNode(2)
    # node1.next.next.next = SllNode(4)
    # node1.next.next.next.next = SllNode(3)

    sub_set = [0, 1]

    print(num_components(node1, sub_set))

