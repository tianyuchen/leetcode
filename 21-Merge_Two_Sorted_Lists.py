# -*- coding: utf-8 -*-
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNode = currentNode = ListNode(0)
        # When l1, l2 both are not vide
        while l1 and l2:
            if l1.val <= l2.val:
                # Link l1 to current node
                currentNode.next = l1
                # Move to next item in l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            currentNode = currentNode.next
        # Link list which isn't empty to current node
        currentNode.next = l1 or l2
        # Return sorted list
        return firstNode.next
