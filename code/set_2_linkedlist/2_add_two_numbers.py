# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Explanation: 342 + 465 = 807
# Input: (2 -> 4 -> 3)  + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# ======================================================================================
# Algorithm:
# linked list
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


# method-1
def add_two_numbers(l1, l2):

    res = SllNode()
    curr = res
    carry = 0

    while l1 or l2 or carry:

        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = SllNode(carry % 10)
        curr = curr.next
        carry = carry//10

    print(str(res.next) + " -> " + str(res.next.next) + " -> " + str(res.next.next.next))
    print([res.next, res.next.next, res.next.next.next])
    return res.next


# Method-2
def add_two_numbers_2(l1, l2):

    res = SllNode(0)
    curr = res
    carry = 0

    while l1 or l2:

        if not l1:
            i = 0
        else:
            i = l1.val
        if not l2:
            j = 0
        else:
            j = l2.val

        lists_sum = i + j + carry

        if lists_sum >= 10:
            remainder = lists_sum % 10
            curr.next = SllNode(remainder)
            carry = 1
        else:
            curr.next = SllNode(lists_sum)
            carry = 0
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        curr.next = SllNode(carry)

    print(str(res.next) + " -> " + str(res.next.next) + " -> " + str(res.next.next.next))
    print([res.next, res.next.next, res.next.next.next])
    return res.next


if __name__ == "__main__":
    node1 = SllNode(3)
    node1.next = SllNode(4)
    node1.next.next = SllNode(2)

    node2 = SllNode(4)
    node2.next = SllNode(6)
    node2.next.next = SllNode(5)
    print("Input Lists:")
    print([node1, node1.next, node1.next.next])
    print([node2, node2.next, node2.next.next])
    print("\n")
    print("Output:")
    print(add_two_numbers(node1, node2))
    print(add_two_numbers_2(node1, node2))



