# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Value: {self.val} Next:{self.next}"

        
def list_to_linkedlist(arr):
    """Convert a Python list to a linked list and return the head."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linkedlist(head):
    """Print a linked list."""
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")
