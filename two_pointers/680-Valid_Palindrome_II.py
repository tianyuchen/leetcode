# -*- coding: utf-8 -*-
'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

# Design a subfunction to check the string is valid or not.
# When we encounter two different characters, we can choose to delete one of them, and check if it’s valid or not.

class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left + 1:right + 1])
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s):
        return s == s[::-1]
