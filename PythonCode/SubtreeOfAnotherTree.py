class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot))

    def isSameTree(self, p: TreeNode, q:TreeNode) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))