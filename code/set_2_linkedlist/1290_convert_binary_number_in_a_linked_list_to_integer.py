# Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# Example 3:
# Input: head = [1]
# Output: 1

# Example 4:
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Example 5:
# Input: head = [0,0]
# Output: 0

# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# ======================================================================================
# Algorithm:
# Bit Manipulation: ??
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=QLny7MZJbno
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def get_decimal_value(head):

    # Input: 1->0->1
    # Output: 5

    res = 0
    while head:
        res = res << 1
        if head.val:
            res = res | 1
        head = head.next

    return res


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(0)
    node1.next.next = SllNode(1)

    print(get_decimal_value(node1))

