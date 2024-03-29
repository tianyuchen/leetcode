# -*- coding: utf-8 -*-
'''
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters
only.
'''

class Solution:
    # Time complexity: O(n)
    # Space complexity:  O(n)
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        # rstrip(): Return a copy of the string with trailing characters removed.
        # The chars argument defaults to removing whitespace
        for i in s.rstrip()[::-1]:
            if i != ' ':
                count += 1
            else:
                return count
        return count


class Solution2:
    # Time complexity: O(n)
    # Space complexity:  O(n)
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


class Solution3:
    # Time complexity: O(n)
    # Space complexity:  O(1)
    def lengthOfLastWord(self, s: str) -> int:
        last_index = len(s) - 1
        while last_index >= 0 and s[last_index] == ' ':
            last_index -= 1

        first_index = last_index
        while first_index >= 0 and s[first_index] != ' ':
            first_index -= 1
        return last_index - first_index
