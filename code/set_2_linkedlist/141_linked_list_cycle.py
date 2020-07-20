# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents
# the position (0-indexed) in the linked list where tail connects to. If pos is -1,
# then there is no cycle in the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
# ======================================================================================
# Algorithm:
# Two pointer: one jumps 1 node at a time and another jumps 2 node at a time
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


# Method-1
def has_cycle(head):

    if not head or not head.next:
        return False

    temp1 = head
    temp2 = head

    while temp2 and temp2.next:

        temp2 = temp2.next.next
        temp1 = temp1.next

        if temp2 == temp1:
            return True

    return False


# ..
def has_cycle_(head):

    if not head or not head.next:
        return False

    temp1 = head
    temp2 = head.next

    while temp2 != temp1:

        if not temp2 or not temp2.next:
            return False

        temp2 = temp2.next.next
        temp1 = temp1.next

    return True


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(3)
    node1.next = SllNode(2)
    node1.next.next = SllNode(0)
    node1.next.next.next = SllNode(-4)

    print(has_cycle(node1))
