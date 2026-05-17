# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_ptr = ListNode()
        curr_head = temp_ptr
        l1 = list1
        l2 = list2

        if not (l1 or l2):
            return None
        
        while l1 and l2:
            if l1.val < l2.val:
                curr_head.next = l1
                l1 = l1.next
            else:
                curr_head.next = l2
                l2 = l2.next
            curr_head = curr_head.next

        if l1:
            curr_head.next = l1
        if l2:
            curr_head.next = l2

        return temp_ptr.next

        