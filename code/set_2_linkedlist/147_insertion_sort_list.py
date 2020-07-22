# Insertion Sort List
# Sort a linked list using insertion sort.
# Algorithm of Insertion Sort:
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# ======================================================================================
# Algorithm:
# TC: O(n^2)
# SC:
# Description: https://www.youtube.com/watch?v=vyeHALAClic
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def insertion_sort_list_1(head):
    dummy = SllNode(0)
    dummy.next = head
    d = dummy
    prev = head
    curr = head

    while curr and curr.next:
        value = curr.next.val
        if curr.val < value:
            curr = curr.next
            continue

        if d.next.val > value:
            d = dummy
        while d.next.val < value:
            d = d.next
        temp = curr.next
        curr.next = temp.next
        temp.next = d.next
        d.next = temp

    print_list(dummy.next)
    return dummy.next


# Method-2
def insertion_sort_list_2(head):

    # Input: 4->2->1->3
    # Output: 1->2->3->4

    if not head:
        return

    dummy = SllNode(0)
    prev = dummy
    curr = head

    while curr:
        nxt = curr.next
        while prev.next and prev.next.val < curr.val:
            prev = prev.next

        curr.next = prev.next
        prev.next = curr
        prev = dummy
        curr = nxt

    print_list(dummy.next)
    return dummy.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


# Method-3
def insertion_sort_list_3(head):

    if not head or not head.next:
        return head

    def insert_node(head, node):

        if not head:
            head = node

        elif head.val >= node.val:
            node.next = head
            head = node

        else:
            curr = head
            while curr.next and curr.next.val < node.val:
                curr = curr.next
            node.next = curr.next
            curr.next = node

    def insertion_sort(head):
        dummy = SllNode(0)
        # temp = None
        curr = head
        while curr:
            nxt = curr.next
            insert_node(dummy, curr)
            curr = nxt
        head = dummy.next

    insertion_sort(head)
    print_list(head)
    return head


# Method-4 ****
def insertion_sort_list(head):

    # Input: 4->2->1->3->
    # dummy: 0 ->1->2->3->4 -> Null
    # Output: 1->2->3->4
    d = dummy = SllNode(0)
    curr = head
    while curr:
        if d and d.val > curr.val:    # reset pointer only when new number is smaller than pointer value
            d = dummy
        while d.next and d.next.val < curr.val:    # classic insertion sort to find position
            d = d.next
        d.next, d.next.next, curr = curr, d.next, curr.next    # insert

    print_list(dummy.next)
    return dummy.next


# Insertion sort
def insertion_sort_(nums):
    for index in range(1, len(nums)):
        value = nums[index]
        i = index - 1
        while i >= 0:
            if value < nums[i]:
                nums[i+1] = nums[i]
                nums[i] = value
                i -= 1
            else:
                break


if __name__ == "__main__":
    node1 = SllNode(4)
    node1.next = SllNode(2)
    node1.next.next = SllNode(1)
    node1.next.next.next = SllNode(3)

    print(insertion_sort_list(node1))

    # Test insertion sort with a list
    # a = [2, 5, 3, 8]
    # print(a)
    # insertion_sort_(a)
    # print(a)
