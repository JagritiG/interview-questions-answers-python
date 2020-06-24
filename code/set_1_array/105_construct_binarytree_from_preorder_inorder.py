# Construct binary tree from preorder and inorder traversal
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# =======================================================================================
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


def build_tree(preorder, inorder):

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        return TreeNode(
            preorder[preorder_start],
            # Recursively build the left subtree
            binary_tree_from_preorder_inorder_helper(
                preorder_start+1, preorder_start+1+left_subtree_size,
                inorder_start, root_inorder_idx),

            # Recursively call the right subtree
            binary_tree_from_preorder_inorder_helper(
                preorder_start+1+left_subtree_size,
                preorder_end, root_inorder_idx+1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))


# Method-2:
def build_tree_2(preorder, inorder):
    if inorder:
        root_idx_in_inorder = inorder.index(preorder[0])
        preorder.pop(0)
        root = TreeNode(inorder[root_idx_in_inorder])

        if root_idx_in_inorder == 0:
            root.left = None
        if root_idx_in_inorder == len(inorder)-1:
            root.right = None
        root.left = build_tree(preorder, inorder[:root_idx_in_inorder])
        root.right = build_tree(preorder, inorder[root_idx_in_inorder+1:])
        return root


if __name__ == "__main__":

    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]

    print(build_tree(pre_order, in_order))


