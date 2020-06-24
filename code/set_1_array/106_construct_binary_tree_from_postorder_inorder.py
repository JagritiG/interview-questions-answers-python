# Construct Binary Tree from Inorder and Postorder Traversal
# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# =========================================================================
# Algorithm:
#
# Time complexity : The time complexity is O(n)-- building the hash table takes O(n) time
# and the recursive reconstruction spends O(1) time per node.
# Space complexity : The space complexity is O(n + h) = O(n) -- the size of the hash table
# plus the maximum depth of the function call stack
# ========================================================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder, postorder):

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_postorder_inorder_helper(inorder_start, inorder_end, postorder_end):
        if postorder_end+1 < 0 or inorder_end+1 <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[postorder[postorder_end]]

        return TreeNode(
            postorder[postorder_end],
            # Recursively build the left subtree
            binary_tree_from_postorder_inorder_helper(
                inorder_start, root_inorder_idx-1, postorder_end-1+root_inorder_idx-inorder_end),

            # Recursively call the right subtree
            binary_tree_from_postorder_inorder_helper(
                root_inorder_idx+1, inorder_end, postorder_end-1))

    return binary_tree_from_postorder_inorder_helper(0, len(inorder)-1, len(postorder)-1)


if __name__ == "__main__":

    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]

    print(build_tree(in_order, post_order))
