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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r, res = 0, 0, 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res


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
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            # Using dictionary and sliding window, checking if a character can
            # be done in O(1)
            # condition start <= usedChar[s[i]] for case "tmmzuxt"
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
