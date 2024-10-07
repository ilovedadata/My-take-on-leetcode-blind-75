class Solution(object):
    def removeNthFromEnd(self, head:ListNode, n:int) -> ListNode:

        dummy = ListNode(0, head)

        l, r = dummy, head

        for i in range(n):
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next 