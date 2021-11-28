# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        original = ListNode()
        answer = original
        while l1 or l2 or carry:
            answer.next = ListNode()
            answer = answer.next
            v1 = 0 if l1 == None else l1.val
            v2 = 0 if l2 == None else l2.val
            val = v1+v2+carry
            carry = val // 10
            answer.val = val%10
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
        return original.next
