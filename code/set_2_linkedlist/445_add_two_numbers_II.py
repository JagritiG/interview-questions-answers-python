# Add Two Numbers II
# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# ======================================================================================
# Algorithm:
# Using two stacks
# TC:
# SC: https://www.youtube.com/watch?v=71NkQBIHxg8
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# method-1 : Using two stack
# TC: O(n)
# SC: O(n)
def add_two_numbers(l1, l2):

    # Input: (7 -> 2 -> 4 -> 3)
    #           + (5 -> 6 -> 4)
    # Input: (7  2  4  3)
    #         + (5  6  4)
    # --------------------
    #         7  8  0  7
    # Output: 7 -> 8 -> 0 -> 7

    res = SllNode()
    curr = res

    # Store list values in the Stack
    stack1 = []
    stack2 = []

    curr1 = l1
    curr2 = l2
    while curr1:
        stack1.append(curr1.val)
        curr1 = curr1.next

    while curr2:
        stack2.append(curr2.val)
        curr2 = curr2.next

    # Pop values from the stacks and add them
    carry = 0
    while stack1 or stack2:

        n1 = stack1[-1] if stack1 else 0
        n2 = stack2[-1] if stack2 else 0

        val_sum = n1 + n2 + carry
        carry = val_sum // 10

        temp = SllNode(val_sum % 10)
        temp.next, curr.next = curr.next, temp

        if stack1:
            stack1.pop()
        if stack2:
            stack2.pop()

    if carry > 0:
        temp = SllNode(carry)
        temp.next, curr.next = curr.next, temp

    # print_list(res.next)
    return res.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(7)
    node1.next = SllNode(2)
    node1.next.next = SllNode(4)
    node1.next.next.next = SllNode(3)

    node2 = SllNode(5)
    node2.next = SllNode(6)
    node2.next.next = SllNode(4)

    print(add_two_numbers(node1, node2))

