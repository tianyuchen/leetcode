# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            commonPrefix = self.common_start(commonPrefix, strs[i])
        return commonPrefix

    def common_start(self, sa, sb):
        def _iter():
            # zip() returns an iterator of tuples based on the iterable object.
            # ex. coordinate = ['x', 'y', 'z']  value = [3, 4, 5, 0, 9]
            # zip(coordinate, value) = [('x', 3), ('y', 4), ('z', 5)]
            for a, b in zip(sa, sb):
                if a == b:
                    # yield will return a generator.
                    yield a
                else:
                    return
        return ''.join(_iter())
