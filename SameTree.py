class Solution(object):
    def isSameTree(self, p: TreeNode, q:TreeNode) -> bool:

        if not p and not q:
            return True
        
        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))