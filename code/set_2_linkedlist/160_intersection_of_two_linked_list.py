# Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the
# two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B,
# it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A;
# There are 3 nodes before the intersected node in B.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the
# two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B,
# it reads as [3,2,4]. There are 3 nodes before the intersected node in A;
# There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B,
# it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Each value on each linked list is in the range [1, 10^9].
# Your code should preferably run in O(n) time and use only O(1) memory.
# ======================================================================================
# Algorithm:
# 1. Calculate length of both LL lists: len1, len2
# 2. Calculate the difference d = |len1 - len2|
# 3. Move d nodes in longer list
# 4. Then move by one step in both lists till head_a == head_b
# TC: O(n)
# SC: O(1)
# Description:
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def get_intersection_node(head_a, head_b):

    # listA:    4->1->8->4->5-> Null
    # listB: 5->6->1->8->4->5-> Null

    if not head_a or not head_b:
        return None

    # Get the size of both the linked lists
    curr_a = head_a
    size_a = 0
    while curr_a:
        curr_a = curr_a.next
        size_a += 1

    curr_b = head_b
    size_b = 0
    while curr_b:
        curr_b = curr_b.next
        size_b += 1

    # Difference of length of two lists
    k = abs(size_a - size_b)
    # print(k)

    # Walk through k nodes of longer list
    curr_a = head_a
    curr_b = head_b
    if size_a > size_b:
        for i in range(k):
            curr_a = curr_a.next

    if size_a < size_b:
        for i in range(k):
            curr_b = curr_b.next

    # Now both lists are equal distant from intersection point
    while curr_a != curr_b:
        curr_a = curr_a.next
        curr_b = curr_b.next

    return curr_a


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(4)
    node1.next = SllNode(1)
    node1.next.next = SllNode(8)
    node1.next.next.next = SllNode(4)
    node1.next.next.next.next = SllNode(5)

    node2 = SllNode(5)
    node2.next = SllNode(6)
    node2.next.next = SllNode(1)
    node2.next.next.next = node1.next.next
    node2.next.next.next.next = node1.next.next.next
    node2.next.next.next.next.next = node1.next.next.next.next

    print(get_intersection_node(node1, node2))

