# -*- coding: utf-8 -*-
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Sets are significantly faster when it comes to determining if an
        # object is present in the set (as in x in s)
        vowels = set(list("aeiouAEIOU"))

        leftPointer = 0
        rightPointer = len(s) - 1
        s = list(s)

        while leftPointer < rightPointer:
            if s[leftPointer] not in vowels:
                leftPointer += 1
            elif s[rightPointer] not in vowels:
                rightPointer -= 1
            else:
                s[rightPointer], s[leftPointer] = s[leftPointer], s[rightPointer]
                leftPointer += 1
                rightPointer -= 1
        return ''.join(s)
