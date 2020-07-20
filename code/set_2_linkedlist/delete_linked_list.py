# Delete Linked List

# Example:
# Input: 1->2->3->4->5->NULL
# Output: None
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


def delete_list(head):
    """Delete a linked list."""

    # 1 -> 2 -> 3 -> 4 -> 5 -> Null

    if not head:
        return head

    curr = head
    while curr:
        temp = curr.next
        del curr.val
        curr = temp


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)

    delete_list(node1)
