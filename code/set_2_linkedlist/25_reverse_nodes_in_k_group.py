# Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=xSJPnb_fveY
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def reverse_k_group(head, k):

    def has_nodes(curr, k):
        temp = curr
        while k > 0 and temp.next:
            k -= 1
            temp = temp.next
        return k == 0

    def reverse_nodes(curr, k):
        temp1 = curr.next
        temp2 = temp1.next
        prev = temp1
        while k > 1:
            temp3 = temp2.next
            temp2.next = prev
            prev = temp2
            temp2 = temp3
            k -= 1

        curr.next = prev
        temp1.next = temp2
        return temp1

    new_node = SllNode()
    new_node.next = head
    curr = new_node
    while has_nodes(curr, k):
        curr = reverse_nodes(curr, k)

    print_list(new_node.next)
    return new_node.next


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
    k = 2   # 2->1->4->3->5
    # k = 3     # 3->2->1->4->5

    print(reverse_k_group(node1, k))

