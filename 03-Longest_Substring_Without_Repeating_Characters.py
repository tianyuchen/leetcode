# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxCount = 0
        characters = []

        for i in s:
            # To check if a character is already in the substring, we can scan
            # the substring, which leads to an O(n^2) algorithm.
            if i in characters:
                maxCount = max(len(characters), maxCount)
                del characters[0:characters.index(i) + 1]

            characters.append(i)

        maxCount = max(len(characters), maxCount)
        return maxCount


class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
