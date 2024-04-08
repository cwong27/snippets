# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        cur1, cur2, carry = l1, l2, 0

        digit = cur1.val + cur2.val
        res = ListNode(digit%10)
        prev = res
        if digit >= 10: 
            carry = 1
        else:
            carry = 0
        cur1, cur2 = cur1.next, cur2.next

        while cur1 or cur2:
            if cur1 and cur2:
                digit = cur1.val + cur2.val + carry
                cur = ListNode(digit%10)
                prev.next = cur
                prev = cur
                if digit >= 10: 
                    carry = 1
                else:
                    carry = 0
                cur1, cur2 = cur1.next, cur2.next
            if cur1 and not cur2:
                digit = cur1.val + carry
                cur = ListNode(digit%10)
                prev.next = cur
                prev = cur
                if digit >= 10: 
                    carry = 1
                else:
                    carry = 0
                cur1 = cur1.next
            if cur2 and not cur1:
                digit = cur2.val + carry
                cur = ListNode(digit%10)
                prev.next = cur
                prev = cur
                if digit >= 10: 
                    carry = 1
                else:
                    carry = 0
                cur2 = cur2.next
        if carry == 1:
            cur = ListNode(1, None)
            prev.next = cur
            prev = cur
        return res