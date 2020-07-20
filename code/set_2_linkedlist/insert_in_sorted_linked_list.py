# Insert in a sorted linked list

# Example:
# Input: 1->2->4, val = 3
# Output: 1->2->3->4
# ======================================================================================
# Algorithm:
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


def insert_sorted_list(head, val):

    # 1->2->4
    #     |
    #     3
    new_node = SllNode(val)

    if not head:
        return new_node

    curr = head
    prev = None
    while curr.val < val:
        prev = curr
        curr = curr.next

    prev.next = new_node
    new_node.next = curr

    # print_list(head)
    return head


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(4)
    val = 3

    print(insert_sorted_list(node1, val))




