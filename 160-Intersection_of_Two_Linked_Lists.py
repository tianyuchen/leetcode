# -*- coding: utf-8 -*-
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time complexity: O(n)
    # Space complexity:  O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = headB if l1 == None else l1.next
            l2 = headA if l2 == None else l2.next
        return l1
