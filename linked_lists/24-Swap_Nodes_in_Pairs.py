# -*- coding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        newHead = prev = ListNode(None)
        while curr and curr.next:
            suiv = curr.next
            curr.next = curr.next.next
            suiv.next = curr
            prev.next = suiv
            prev = curr
            curr = curr.next
        return newHead.next
