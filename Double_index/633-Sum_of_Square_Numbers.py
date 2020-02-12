# -*- coding: utf-8 -*-
'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: 3
Output: False
'''

class Solution(object):
    # Time complexity: O(sqrt(target))
    # Space complexity: O(1)
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = (int)(math.sqrt(c))
        
        while a <= b:
            sum = a * a + b * b
            if sum == c:
                return True
            elif sum > c:
                b -= 1
            else:
                a += 1
        return False
