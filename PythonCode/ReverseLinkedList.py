class Solution(object):

    def reversell(self, head:ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
    
        return prev