# Partition List
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=pfShpfdW_wc
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def partition(head, x):

    # 1->4->3->2->5->2-> Null
    # x = 3
    # 1->2->2->4->3->5-> Null

    if not head:
        return head

    before = SllNode(0)
    after = SllNode(0)
    temp_bfr = before
    temp_aftr = after
    curr = head

    while curr:
        if curr.val >= x:
            after.next = curr
            after = after.next

        else:
            before.next = curr
            before = before.next

        curr = curr.next

    after.next = None
    before.next = temp_aftr.next

    # print_list(temp_bfr.next)
    return temp_bfr.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(4)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(2)
    node1.next.next.next.next = SllNode(5)
    node1.next.next.next.next.next = SllNode(2)
    x = 3

    print(partition(node1, x))
