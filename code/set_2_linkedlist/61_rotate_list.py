# Rotate List
# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
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


# Method-1
def rotate_right_1(head, k):
    """Rotate a linked list to the right by k places."""

    # 1 -> 2 -> 3 -> 4 -> 5 -> Null
    # 4 -> 5 -> 1 -> 2 -> 3 -> Null
    if not head:
        return head

    # Size of the list
    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next

    dummy = SllNode(0)
    dummy.next = head
    temp = dummy
    count = 0
    while count < k % size:
        curr = dummy.next
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        curr.next = temp.next
        temp.next = curr
        prev.next = None
        count += 1

    # print_list(dummy.next)
    return dummy.next


# Method-2
def rotate_right(head, k):
    """Rotate a linked list to the right by k places."""

    # 1 -> 2 -> 3 -> 4 -> 5 -> Null
    # 4 -> 5 -> 1 -> 2 -> 3 -> Null
    if not head:
        return head

    # Size of the list
    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next

    dummy = SllNode(0)
    dummy.next = head
    temp = dummy

    curr_1 = dummy
    curr_2 = dummy

    k = k % size
    position = 1

    while position <= size-k:
        curr_1 = curr_1.next
        position += 1

    while curr_2.next:
        curr_2 = curr_2.next

    curr_2.next = temp.next
    temp.next = curr_1.next
    curr_1.next = None

    print_list(dummy.next)
    return dummy.next


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
    k = 2

    # print("Input:")
    # print_list(node1)
    print("Output:")
    print(rotate_right(node1, k))


