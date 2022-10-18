# -*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number
0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            res = v1 + v2 + carry
            carry = res // 10
            res = res % 10
            cur.next = ListNode(res)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        hasCarry = False
        headNode = None
        previousNode = None

        while l1 != None or l2 != None or hasCarry:
            total = 0

            if l1 is not None:
                total += l1.val
            if l2 is not None:
                total += l2.val
            if hasCarry:
                total += 1

            if total < 10:
                hasCarry = False
                currentNode = ListNode(total)
            else:
                hasCarry = True
                currentNode = ListNode(total % 10)

            if headNode is None:
                headNode = currentNode
            else:
                previousNode.next = currentNode

            previousNode = currentNode
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return headNode
