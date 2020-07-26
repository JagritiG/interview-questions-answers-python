# Remove Zero Sum Consecutive Nodes from Linked List
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0
# until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.

# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.

# Example 2:
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]

# Example 3:
# Input: head = [1,2,3,-3,-2]
# Output: [1]
# ======================================================================================
# Algorithm:
# TC:
# SC:
# Description:  https://www.youtube.com/watch?v=tss5biw6ctI
# ========================================================================================


class SllNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


# Method-1
def remove_zero_sum_sublists(head):

    # Input:                       1 -> 2 -> -3 -> 3 -> 1 -> Null
    # ht key (sum: 0):         0   1    3     0    3    4
    # ht val: (ll node: dummy):    1 -> 2 -> -3 -> 3 -> 1 -> Null
    # Output: [3,1] or [1,2,1]

    dummy = SllNode(0)
    dummy.next = head

    ht = dict()
    ht[0] = dummy
    acc_sum = 0

    while head:
        acc_sum += head.val
        if acc_sum in ht:

            # remove entries
            temp = ht[acc_sum].next
            temp_sum = acc_sum
            while temp != head:
                temp_sum += temp.val
                del ht[temp_sum]
                temp = temp.next

            # build next link
            ht[acc_sum].next = head.next

        else:
            # hash table entry
            ht[acc_sum] = head

        head = head.next

    # print_list(dummy.next)
    return dummy.next


def print_list(llist):
    curr = llist
    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":

    node1 = SllNode(1)
    node1.next = SllNode(2)
    node1.next.next = SllNode(-3)
    node1.next.next.next = SllNode(3)
    node1.next.next.next.next = SllNode(1)

    print(remove_zero_sum_sublists(node1))
