from utils import *
from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Divide the linked list into two halves
        slow, fast = head, head.next 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        # Reverese the second half
        second = slow.next 
        prev = slow.next = None 
        while second: 
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp 


        # Merge the two halves
        first, second = head, prev 
        while second: 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1
            first, second = tmp1, tmp2

        return head



        

head = list_to_linkedlist([2,4,6,8])
new_head = Solution().reorderList(head)
print_linkedlist(new_head)