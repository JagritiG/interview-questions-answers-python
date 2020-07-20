# Sort List
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# ======================================================================================
# Algorithm:
# Merge sort
# TC: O(nlogn)
# SC: O(1)
# Description: https://www.youtube.com/watch?v=pNTc1bM1z-4
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def sort_list(head):

    # 4->2->1->3-> Null
    # 1->2->3->4-> Null

    if not head or not head.next:
        return head

    # get the middle of the list
    mid = temp1 = temp2 = head
    while temp2 and temp2.next:
        temp1 = mid
        mid = mid.next
        temp2 = temp2.next.next

    temp1.next = None

    left = sort_list(head)
    right = sort_list(mid)

    def merge_list(l1, l2):

        new_list = SllNode()
        curr = new_list

        if not l1:
            return l2
        if not l2:
            return l1

        # Traverse two lists, compare, and merge them
        while l1 and l2:

            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = curr.next

            else:
                curr.next = l2
                curr = l2
                l2 = curr.next

            curr.next = l1 or l2

        return new_list.next

    return merge_list(left, right)


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(4)
    node1.next = SllNode(2)
    node1.next.next = SllNode(1)
    node1.next.next.next = SllNode(3)

    print(sort_list(node1))
