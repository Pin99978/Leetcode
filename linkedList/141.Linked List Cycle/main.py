# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Run with Floyd Cycle Detection Algorithm 
# time: O(n) 76.73%


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        slow = head
        fast = head

        # go with Floyd Cycle Detection Algorithm
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False        
