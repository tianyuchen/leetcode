# -*- coding: utf-8 -*-
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


class Solution2:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            diff = curr.next
            while diff and diff.val == curr.val:
                diff = diff.next
            curr.next = diff
            curr = diff
        return head
