# Given a non-negative integer represented as non-empty a singly linked list of
# digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are sorted such that the most significant digit is at the head of the list.

# Example:
# Input: [1, 2, 3]
# Output: [1, 2, 4]
# ======================================================================================
# Algorithm:
#
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


# method-1 :
def plus_one(head):

    # Input: (1 -> 2 -> 3)
    #                 + 1
    # Input: (1  2  3)
    #             + 1
    # --------------------
    #         1  2  4
    # Output: 1 -> 2 -> 4

    res = SllNode(1)

    stack = []
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next

    curr = res
    val_sum = stack[-1] + 1
    carry = val_sum // 10

    temp = SllNode(val_sum % 10)
    temp.next, curr.next = curr.next, temp
    stack.pop()

    while stack:
        val_sum = stack.pop() + carry
        carry = val_sum // 10
        temp = SllNode(val_sum % 10)
        temp.next, curr.next = curr.next, temp

    if carry > 0:
        print_list(res)
        return res

    else:
        print_list(res.next)
        return res.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(9)
    node1.next = SllNode(9)
    node1.next.next = SllNode(9)

    # print_list(node1)
    print(plus_one(node1))
