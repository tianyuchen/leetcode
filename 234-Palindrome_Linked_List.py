# -*- coding: utf-8 -*-
'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        # find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second part
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first part and the second part
        while node and head:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True
