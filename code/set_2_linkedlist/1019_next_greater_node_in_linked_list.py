# Next Greater Node In Linked List
# We are given a linked list with head as the first node.
# Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val
# such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.
# If such a j does not exist, the next larger value is 0.

# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
# Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent
# the serialization of a linked list with a head node value of 2, second node value of 1,
# and third node value of 5.

# Example 1:
# Input: [2,1,5]
# Output: [5,5,0]

# Example 2:
# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]

# Example 3:
# Input: [1,7,5,1,9,2,5,1]
# Output: [7,9,9,9,0,5,0,0]

# Note:
# 1 <= node.val <= 10^9 for each node in the linked list.
# The given list has length in the range [0, 10000].
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description: https://www.youtube.com/watch?v=uFso48YRRao, 
# https://www.youtube.com/watch?v=wVsGnpXoxPI
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def next_larger_nodes(head):

    # Ex-1
    # Input: 2 -> 1 -> 5 -> Null
    # Output: [5, 5, 0]

    # Ex-2
    # Input: 2 -> 7 -> 4 -> 3 -> 5 -> Null
    # Output: [7 0,5,5,0]

    curr = head
    new_list = []
    while curr:
        new_list.append(curr.val)
        curr = curr.next

    res = [0] * len(new_list)

    stack = []
    for i, e in enumerate(new_list):
        while stack and new_list[stack[-1]] < e:
            res[stack.pop()] = e

        stack.append(i)

    return res


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":

    node1 = SllNode(2)
    node1.next = SllNode(7)
    node1.next.next = SllNode(4)
    node1.next.next.next = SllNode(3)
    node1.next.next.next.next = SllNode(5)

    print(next_larger_nodes(node1))

