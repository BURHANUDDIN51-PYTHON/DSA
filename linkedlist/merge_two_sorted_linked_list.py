from utils import * 
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        # Return the list if there are none values 
        if not list1:
            return list2
        if not list2:
            return list1
        

        # Maintain two pointers 
        i = list1
        j = list2

        # Create the head pointer 
        head = None 
        if i.val <= j.val:
            head = i 
            i = i.next 
        else:
            head = j
            j = j.next 

        prev = head
        while i and j: 
            if i.val <= j.val: 
                newNode = ListNode(i.val)
                i = i.next 
            else:
                newNode = ListNode(j.val)
                j = j.next 

            # Maintain the prev 
            prev.next = newNode
            prev = newNode


        # Fill up the rest of the values 
        while i: 
            prev.next = ListNode(i.val)
            prev = prev.next
            i = i.next
        while j: 
            prev.next = ListNode(j.val)
            prev = prev.next
            j = j.next


        return head


list1 = [1,2,4]
list2 = [1,3,5]
head1, head2 = list_to_linkedlist(list1), list_to_linkedlist(list2)
new_head = Solution().mergeTwoLists(head1, head2)
print_linkedlist(new_head)