class Solution(object):

    def mergells(self, list1:ListNode, list2:ListNode) -> ListNode:
        new_head = ListNode()
        traverser = new_head

        while list1 and list2:
            if list1.val < list2.val:
                traverser.next = list1
                list1 = list1.next
            else:
                traverser.next = list2
                list2 = list2.next
            
            traverser = traverser.next 
        
        if list1:
            traverser.next = list1
        
        if list2:
            traverser.next = list2
        
        return new_head.next