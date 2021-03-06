# Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
# Return a deep copy of the list.

# The Linked List is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to,
# or null if it does not point to any node.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Example 4:
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.

# Constraints:
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC: O(1)
# Description: https://www.youtube.com/watch?v=L2wOEvjCjwA
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None, random = None):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def copy_random_list(head):

    # Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

    # Copy nodes: copy ith node and add it next to the ith node
    curr = head
    while curr:
        temp = curr.next
        copy = SllNode(curr.val, curr.next, curr.random)
        curr.next = copy
        copy.next = temp
        curr = temp

    # Get the copy of randoms
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next

        curr = curr.next.next     # skip all the copied node while traversing the list

    # Get the copied list nodes
    new_node = SllNode(0)
    prev = new_node
    curr = head
    while curr:
        prev.next = curr.next
        curr.next = curr.next.next
        curr = curr.next
        prev = prev.next

    # print_list(new_node.next)
    return new_node.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    node1 = SllNode(7)
    node2 = node1.next = SllNode(13)
    node3 = node2.next = SllNode(11)
    node4 = node3.next = SllNode(10)
    node5 = node4.next = SllNode(1)

    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    print(copy_random_list(node1))
