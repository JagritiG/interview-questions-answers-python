# Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?
# ======================================================================================
# Algorithm:
# Stack, two pointer
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=UNun8zP0bQc
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def is_palindrome(head):

    # 1->2->2->1 : True
    # 1->2 : False

    if not head:
        return True

    temp1 = temp2 = head
    stack = []

    while temp2 and temp2.next:

        stack.append(temp1.val)
        temp1 = temp1.next
        temp2 = temp2.next.next

    if temp2:
        temp1 = temp1.next

    while temp1 and stack:
        if stack.pop() != temp1.val:
            return False
        temp1 = temp1.next

    return True


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    # node1.next.next = SllNode(2)
    # node1.next.next.next = SllNode(1)

    print(is_palindrome(node1))
