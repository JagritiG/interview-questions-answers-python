# Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Example 2:
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# Note:
# The number of nodes in the given list will be between 1 and 100.
# ======================================================================================
# Algorithm:
# two pointers, fast and slow
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


def middle_node(head):

    if not head:
        return True

    temp1 = head
    temp2 = head

    while temp2 and temp2.next:

        temp1 = temp1.next
        temp2 = temp2.next.next

    if temp2:
        return temp1

    else:
        return temp1


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)
    node1.next.next.next.next.next = SllNode(6)

    print(middle_node(node1))
