# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not low:
            return high
        if not high:
            return low
        t=TreeNode(low.val+high.val)
        t.left=rangeSumBST(low.left,high.left)
        t.right=rangeSumBST(low.right,high.right)
        return t
    
res=Solution()
res.rangeSumBST([10,5,15,3,7,0,18], 7, 15)
