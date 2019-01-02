# -*- coding: utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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
