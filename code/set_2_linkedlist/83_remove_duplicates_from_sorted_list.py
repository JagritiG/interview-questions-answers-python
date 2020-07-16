# Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3
# ======================================================================================
# Algorithm:
# Hash table
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


def delete_duplicates(head):

    # 1->1->2->3->3-> Null
    if not head:
        return head

    curr = head
    prev = None

    duplicates = dict()

    while curr:

        if curr.val in duplicates:

            # Remove the node
            prev.next = curr.next
            curr = None

        else:  # If val not present in hash table
            duplicates[curr.val] = 1
            prev = curr

        curr = prev.next

    print_list(head)
    return head


def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(1)
    node1.next.next = SllNode(2)
    node1.next.next.next = SllNode(3)
    node1.next.next.next.next = SllNode(3)

    # print("Input:")
    # print_list(node1)
    print("Output:")
    print(delete_duplicates(node1))
