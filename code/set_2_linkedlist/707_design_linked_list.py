# Design Linked List
# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
# and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more
# attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement these functions in your linked list class:
# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
# the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list.
# If index equals to the length of linked list, the node will be appended to the end of linked list.
# If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

# Example:
# Input:
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# Output:
# [null,null,null,null,2,null,3]

# Explanation:
# MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3

# Constraints:
# 0 <= index,val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
# ============================================================================================
# Algorithm:
#
# TC:
# SC: https://www.youtube.com/watch?v=nrUCaiCG29w
# ============================================================================================


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1

        curr = self.head
        position = 0
        while position < index and curr.next:
            curr = curr.next
            position += 1

        return curr.val

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.size += 1

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """

        # When given position is greater than size of list
        if index > self.size:
            return

        # when add at first position
        elif index == 0:
            self.add_at_head(val)

        # when add at last position
        elif index == self.size:
            self.add_at_tail(val)

        else:
            new_node = ListNode(val)
            curr = self.head
            position = 0
            while position < index - 1:
                curr = curr.next
                position += 1
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # When given position is greater than size of list
        if index >= self.size:
            return

        # Delete first node
        if index == 0:
            self.head = self.head.next

        # Delete nth node
        else:
            curr = self.head
            position = 0
            while position < index - 1:
                curr = curr.next
                position += 1
            curr.next = curr.next.next
        self.size -= 1

    # =========================================================
    # Utility function to get size of the linked list
    def size_list(self):
        """Size of the Linked List."""
        size = 0
        curr = self.head
        while curr:
            curr = curr.next
            size += 1
        return size

    # Utility function to print the linked list
    def print_list(self):
        """Print all the elements of the Linked List."""
        curr = self.head
        while curr:
            print(curr.val,)
            curr = curr.next


if __name__ == "__main__":

        # Input:
        # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
        # [[],[1],[3],[1,2],[1],[1],[1]]
        # Output:
        # [null,null,null,null,2,null,3]

        sll = MyLinkedList()
        # sll.print_list()
        # print("\n")

        sll.add_at_head(1)
        sll.add_at_tail(3)
        # sll.print_list()
        # print("\n")

        sll.add_at_index(1, 2)
        # sll.print_list()
        # print("\n")
        #
        # print(sll.get(1))
        # sll.print_list()
        # print("\n")
        #
        # sll.delete_at_index(1)
        # sll.print_list()
        # print("\n")
        #
        print(sll.get(1))
        sll.print_list()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
