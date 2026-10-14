# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a = 0
        sum = l1.val + l2.val
        res = ListNode(sum % 10, None)
        l1 = l1.next
        l2 = l2.next
        sum //= 10
        head = res
        while(l1 != None or l2 != None):
            if (l1 == None):
                sum += l2.val
                res.next = ListNode(sum % 10, None)
                res = res.next
                l2 = l2.next
                sum //= 10
            elif (l2 == None):
                sum += l1.val
                res.next = ListNode(sum % 10, None)
                res = res.next
                l1 = l1.next
                sum //= 10
            else:
                sum += l1.val + l2.val
                res.next = ListNode(sum % 10, None)
                l1 = l1.next
                l2 = l2.next
                sum //= 10
                res = res.next
        if(sum != 0):
            res.next = ListNode(sum % 10, None)
            res = res.next
        return head
