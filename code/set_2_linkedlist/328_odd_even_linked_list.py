# Odd Even Linked List
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Constraints:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].
# ======================================================================================
# Algorithm:
#
# TC: O(n)
# SC: in-place O(1)
# Description: https://www.youtube.com/watch?v=QcSLh0JtwFk
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method - 1 :
def odd_even_list_1(head):

    # Input: 1->2->3->4->5->NULL
    # Output: 1->3->5->2->4->NULL
    if not head:
        return head

    odd = SllNode(0)
    curr_odd = odd
    even = SllNode(0)
    curr_even = even
    curr = head
    is_odd = True

    while curr:

        if is_odd:
            curr_odd.next = curr
            curr_odd = curr_odd.next

        else:
            curr_even.next = curr
            curr_even = curr_even.next

        is_odd = not is_odd
        curr = curr.next

    curr_even.next = None
    curr_odd.next = even.next
    print_list(odd.next)
    return odd.next


# method-2
def odd_even_list(head):

    # Input: 1->2->3->4->5->NULL
    # Output: 1->3->5->2->4->NULL
    if not head:
        return head

    odd = SllNode(0)
    curr_odd = odd
    even = SllNode(0)
    curr_even = even
    curr = head

    count = 1
    while curr:

        if count % 2 == 0:
            curr_even.next = curr
            curr_even = curr_even.next
        else:
            curr_odd.next = curr
            curr_odd = curr_odd.next
        curr = curr.next
        count += 1

    curr_even.next = None
    curr_odd.next = even.next
    print_list(odd.next)
    return odd.next


def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)

    print(odd_even_list(node1))
