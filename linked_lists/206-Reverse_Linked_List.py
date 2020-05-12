# -*- coding: utf-8 -*-
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# recursive solution
class Solution2:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseNode(head)

    def reverseNode(self, node, prev = None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self.reverseNode(next, node)
