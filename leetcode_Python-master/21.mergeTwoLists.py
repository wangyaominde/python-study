# -*- coding: utf-8 -*-
# @Author: wangyaominde
# @Date: 2018-12-16 02:34:36
# @Last Modified by:   wangyaominde
# @Last Modified time: 2018-12-16 02:34:36


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = temp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return head.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)


test = Solution()
test.mergeTwoLists(a, b)
