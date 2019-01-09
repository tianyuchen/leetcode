# -*- coding: utf-8 -*-
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversedNum = int(str(abs(x))[::-1])

        if x < 0:
            x = -1 * reversedNum
        else:
            x = reversedNum

        if - 2 ** 31 - 1 < x < 2 ** 31:
            return x
        else:
            return 0



class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            (q, r) = divmod(x, 10)
            num = num * 10 + r
            x = q

        if - 2 ** 31 - 1 < num < 2 ** 31:
            return num * sign
        else:
            return 0
