# Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# Return the linked list sorted as well.

# Example 1:
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Example 2:
# Input: 1->1->1->2->3
# Output: 2->3
# ======================================================================================
# Algorithm:
# Hash table, iterative in-place
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


# Method - 1 : using hash table
def delete_duplicates_ht(head):

    # 1->2->3->3->4->4->5 Null
    # 1->2->5
    if not head:
        return head

    duplicates = dict()

    curr = head
    while curr:

        if curr.val not in duplicates:
            duplicates[curr.val] = [curr.val]

        else:  # If val not present in hash table
            duplicates[curr.val].append(curr.val)

        curr = curr.next

    curr = head
    prev = None
    while curr:

        if len(duplicates[curr.val]) > 1:

            if curr == head:
                head = curr.next
                curr = head

            else:
                prev.next = curr.next
                curr = None
                curr = prev.next
        else:
            prev = curr
            curr = curr.next

    # print(duplicates)
    print_list(head)
    return head


# Method - 2 : Iterative
def delete_duplicates(head):

    # 1->2->3->3->4->4->5 Null
    # 1->2->5
    if not head:
        return head

    temp = prev = SllNode(0)
    temp.next = head
    curr = head

    while curr and curr.next:
        if curr.val != curr.next.val:
            prev = curr
            curr = curr.next

        else:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            curr = curr.next
            prev.next = curr

    print_list(temp.next)
    return temp.next


def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(3)
    node1.next.next.next = SllNode(3)
    node1.next.next.next.next = SllNode(4)
    node1.next.next.next.next.next = SllNode(4)
    node1.next.next.next.next.next.next = SllNode(5)

    # print("Input:")
    # print_list(node1)
    print("Output:")
    print(delete_duplicates(node1))
