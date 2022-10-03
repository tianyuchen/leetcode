# -*- coding: utf-8 -*-
'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents
the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(n)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        node = head

        visited.add(node)

        while node and node.next:
            node = node.next
            if node in visited:
                return True
            visited.add(node)
        return False


class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
             # If there's a cycle the fast will catch up with the slow, there
             # will be a meet up with each other.
            if slow == fast:
                return True
        return False
