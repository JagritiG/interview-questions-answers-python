# Delete N nodes after M nodes of a linked list
# Given a linked list and two integers M and N. Traverse the linked list such that
# you retain M nodes then delete next N nodes, continue the same till end of the linked list.

# Example1:
# Input:
# Linked List: 1->2->3->4->5->6->7->8
# M = 2, N = 2
# Output:
# Linked List: 1->2->5->6

# Example2:
# Input:
# Linked List: 1->2->3->4->5->6->7->8->9->10
# M = 3, N = 2
# Output:
# Linked List: 1->2->3->6->7->8

# Example3:
# Input:
# Linked List: 1->2->3->4->5->6->7->8->9->10
# M = 1, N = 1
# Output:
# Linked List: 1->3->5->7->9
# ======================================================================================
# Algorithm:  ???
# TC:
# SC:
# Description:
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


def delete_n_nodes_after_m_nodes(head, m, n):

        # 1->2->3->4->5->6->7->8-> Null
        # m = 2, n = 2
        # 1->2->5->6-> Null
        curr = head

        while curr:

            # Skip m nodes
            for i in range(1, m):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                    return

            # Start from next node and delete n nodes
            nxt_node = curr.next
            for i in range(1, n+1):
                if nxt_node is None:
                    break
                nxt_node = nxt_node.next

            # Link the previous list with remaining nodes
            curr.next = nxt_node

            # Set Current pointer for next iteration
            curr = nxt_node

        print_list(head)
        return head


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
    node1.next.next.next.next.next = SllNode(6)
    node1.next.next.next.next.next.next = SllNode(7)
    node1.next.next.next.next.next.next.next = SllNode(8)
    node1.next.next.next.next.next.next.next.next = SllNode(9)
    node1.next.next.next.next.next.next.next.next.next = SllNode(10)
    m = 5
    n = 2

    print(delete_n_nodes_after_m_nodes(node1, m, n))

