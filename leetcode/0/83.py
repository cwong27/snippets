# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return head
        cur_next = None
        while current.next is not None:
            cur_next = current.next
            if current.val != cur_next.val:
                current = cur_next
            elif current.val == cur_next.val:
                current.next = cur_next.next
        return head
        