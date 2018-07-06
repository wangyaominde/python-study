global flag1,flag2,flag3
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
            
        global flag1
        global flag2
        l3.val = l1.val + l2.val
        l3.next = ListNode(l1.next.val + l2.next.val)
        l3.next.next = ListNode(l1.next.next.val + l2.next.next.val)
        if l3.val>=10:
            flag1 = 1
            l3.val = l3.val%10
        if l3.next.val>=10:
            flag2 = 1
            l3.next.val = l3.next.val%10
        if flag2==1:
            l3.next.next.val = l3.next.next.val+1
        return l3.val,l3.next.val,l3.next.next.val


l3 = ListNode(0)
l3.next = ListNode(0)
l3.next.next = ListNode(0)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


a=Solution()
print(a.addTwoNumbers(l1,l2))
