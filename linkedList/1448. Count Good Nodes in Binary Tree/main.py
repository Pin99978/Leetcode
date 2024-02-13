# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# run with BFS 
# 115ms / 31.37mb 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        cur = root.val
        cnt = 1
        max_num = cur
        def dfs(node , max_num  ):
            nonlocal cnt
            if  node:                
                   
                cur = node.val
                if cur >= max_num:
                    cnt += 1               
                    max_num = cur
                
                dfs(node.left , max_num )
                dfs(node.right, max_num )
            else:
                pass

        dfs(root.left  , max_num) 
        dfs(root.right , max_num) 
        return cnt
