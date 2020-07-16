# Delete Node in a Linked List
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.
# ======================================================================================
# Algorithm:
# iterative in-place
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
def delete_node(head, node):

    # 4->5->1->9-> Null, node = 5
    # 4->1->9
    if not head:
        return head

    # if first node is the target node
    if head.val == node:
        head = head.next

    # If target node is not head node
    else:
        curr = head
        prev = None

        while curr.next:

            if curr.val == node:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

    # print(duplicates)
    print_list(head)
    return head


# Leetcode: solution
def delete_node_1(self, node):
    node.val = node.next.val
    node.next = node.next.next


def print_list(llist):
        curr = llist
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(4)
    node1.next = SllNode(5)
    node1.next.next = SllNode(1)
    node1.next.next.next = SllNode(9)
    n = 5


    # print("Input:")
    # print_list(node1)
    print("Output:")
    print(delete_node(node1, n))
