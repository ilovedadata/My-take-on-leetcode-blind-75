class Solution(object):
    def reorderList(self, head:ListNode) -> ListNode:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = None 
        slow.next = None 

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        reversed_head = prev
        straight_head = head    

        while reversed_head: 
            tmp1, tmp2 = straight_head.next, reversed_head.next
            straight_head.next = reversed_head
            reversed_head.next = tmp1
            straight_head, reversed_head = tmp1, tmp2