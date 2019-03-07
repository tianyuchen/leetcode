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

        j, k = 0, 0
        T = [-1] * len(needle)

        while j < len(haystack):
            if needle[k] == haystack[j]:
                j += 1
                k += 1

                if k == len(needle):
                    P[nP] = j - k
                    nP = nP + 1
                    k = T[k]
            else:
                k = T[k]
                if k < 0:
                    j = j + 1
                    k = k + 1
