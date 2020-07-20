# Linked List Cycle II
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position
# (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# Note: Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Follow-up:
# Can you solve it without using extra space?
# ======================================================================================
# Algorithm:
# Two pointers
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=bgmPP4n8sIM
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def detect_cycle(head):

    if not head or not head.next:
        return None

    temp1 = head
    temp2 = head

    while temp2 and temp2.next:

        temp2 = temp2.next.next
        temp1 = temp1.next

        if temp2 == temp1:

            curr = head
            while curr != temp1:
                temp1 = temp1.next
                curr = curr.next

            return temp1

    return None


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

    print(detect_cycle(node1))
