# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        dummy = ListNode()
        cur = dummy
        carry = 0

        while r1 or r2 or carry:
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0

            total = v1 + v2 + carry

            carry = total // 10
            total = total % 10

            cur.next = ListNode(total)
            cur = cur.next

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None
        
        return self.reverseList(dummy.next)