# -*- coding: utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for i in s:
            # when stack is vide
            if not stack:
                stack.append(i)
            # when i is the key in mapping and the last element in stack is its pair bracket
            elif i in mapping and stack[-1] == mapping[i]:
                stack.pop()
            else:
                stack.append(i)
        # If the stack is empty, we have a valid expression.
        return not stack
