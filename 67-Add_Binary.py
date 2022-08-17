# -*- coding: utf-8 -*-
'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a and a.pop() == '1':
                carry += 1
            if b and b.pop() == '1':
                carry += 1
            res.append('0' if carry % 2 == 0 else '1')
            carry >>= 1
        return ''.join(res)[::-1] 


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, 2) + int(b, 2)
        res = str("{0:b}".format(c))
        return res
