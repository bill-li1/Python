class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(1)
b = a

b.val = 2
b.next = ListNode(3)
b = b.next
b.next = ListNode(4)
b = b.next
b.next = ListNode(5)
b = b.next





while a.next:
    print(a.val)
    a = a.next
