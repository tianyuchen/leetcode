# -*- coding: utf-8 -*-
'''
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_to_i = max_now = nums[0]
        for i in nums[1:]:
            max_to_i = max(i, max_to_i + i)
            max_now = max(max_now, max_to_i)
        return max_now
