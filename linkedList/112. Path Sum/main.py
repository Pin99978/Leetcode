# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 36ms  / 17.38MB
#run with BFS medhot

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # go BFS
        if not root:
            return False

        
        cur_sum = 0 
        def BFS(node, cur_sum):
            
            if node :
                
                cur_sum+=node.val
                # check if last node
                if not node.left and not node.right:
                    if cur_sum == targetSum:

                        return True
                    else:
                        return False
                
                return BFS(node.left,cur_sum ) or BFS(node.right,cur_sum)
            else:
                pass        
        return BFS(root , cur_sum)
