# -*- coding: utf-8 -*-
'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''
# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        while left <= right:
            mid = math.ceil(left + (right - left) / 2)
            print(left, right, mid)
            if mid == x/mid:
                return mid
            elif mid < x / mid:
                left = mid + 1
            else:
                right = mid - 1

        return right

# Brute force
class Solution:
    def mySqrt(self, x: int) -> int:
        sr = 1
        while True:
            if sr * sr > x:
                return sr -1
            else:
                sr += 1
