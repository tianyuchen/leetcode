# -*- coding: utf-8 -*-
'''
The count-and-say sequence is the sequence of integers with the first five terms
as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say
sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

def countAndSay(sequence):
    res = ''
    count = 1
    sequence += '0'
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next = sequence[i + 1]
        if current != next:
            res += str(count) + current
            count = 1
        else:
            count += 1
    return res

print(countAndSay("111221"))
