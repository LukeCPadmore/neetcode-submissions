# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_ptr = ListNode(next = None)
        total_head = temp_ptr
        carry = 0

        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10 # New digit in number
            carry = (l1.val + l2.val + carry) // 10 # Carry digit
            total_head.next = ListNode(val,None)
            total_head = total_head.next
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            if l1:
                s = l1
            else:
                s  = l2
            while s:
                val = (s.val + carry) % 10
                carry = (s.val + carry) // 10
                total_head.next = ListNode(val,None)
                total_head = total_head.next
                s = s.next
        
        if carry > 0:
            total_head.next = ListNode(carry,None)
        
        return temp_ptr.next
        






            



        



            


        