"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

"""

"""
Approach: Binary search 
- If x is less than 2, return x 
- Set left and right pointers to 1 and x/2, respectively 
- While left <= right: 
    - Set mid to the average of left and right
    - If mid * mid is greater than x, set right to mid - 1 
    - Else, set left to mid + 1 
- Return right

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: 
            return x 
        
        l, r = 1, x//2 
        while l <= r: 
            m = (l + r) // 2 
            if m * m < x: 
                l = m + 1 
            elif m * m > x: 
                r = m - 1 
            else: 
                return m 
        return r 