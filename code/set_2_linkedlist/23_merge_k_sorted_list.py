# Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# ======================================================================================
# Algorithm:
# Min heap
# 1. Create a min head
# 2. Traverse all the lists and insert these values in min heap
# 3. Create a new node; remove values from min heap, and insert
# into the new list node.
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=zLcNwcR6yO4
# ========================================================================================
import heapq


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# method
def merge_k_lists(lists):

    # Create a min heap
    min_heap = []
    heapq.heapify(min_heap)

    # Traverse the list of lists and insert values into heap
    for head in lists:
        while head:
            heapq.heappush(min_heap, head.val)
            head = head.next

    new_node = SllNode()
    head = new_node
    while min_heap:
        head.next = SllNode(heapq.heappop(min_heap))
        head = head.next

    # print_list(new_node.next)
    return new_node.next


def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(4)
    node1.next.next = SllNode(5)

    node2 = SllNode(1)
    node2.next = SllNode(3)
    node2.next.next = SllNode(4)

    node3 = SllNode(2)
    node3.next = SllNode(6)

    lst = [node1, node2, node3]
    print(merge_k_lists(lst))




