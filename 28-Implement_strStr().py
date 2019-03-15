# -*- coding: utf-8 -*-
'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution1:
    # Time complexity: O(n * m)
    # Space complexity:  O(1)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


class Solution2:
    # Time complexity: O(n)
    # Space complexity:  O(1)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


class Solution3:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None:
            return -1

        #generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            #needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]

        #check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1
