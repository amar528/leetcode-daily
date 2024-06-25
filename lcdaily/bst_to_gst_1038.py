from lcdaily.treenode import TreeNode


class Solution:
    def __init__(self):
        self.val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(node):

            # base case - null node
            if not node:
                return

            # recurse all the way right
            dfs(node.right)

            # all values to the right will be greater, update the total
            self.val += node.val
            node.val = self.val

            # recurse left
            dfs(node.left)

        # start dfs from the root node
        dfs(root)
        return root
