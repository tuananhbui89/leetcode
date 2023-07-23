"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

"""
Approach: Dynamic Programming 

Analyze: 
- If n == 1, only 1 way to climb to the top 
- If n == 2, only 2 ways to climb to the top. 1 step + 1 step or 2 steps 
- If n == 3, dp(3) = dp(2) + dp(1). Where dp(1) is number of ways to climb to the top with 1 step and dp(2) is number of ways to climb to the top with 2 steps. 
If start at dp(2) then there is only 1 way to climb to the top with 1 step. 
If start at dp(1) then there is 1 way to climb to the top with 2 steps (without passing dp(2) because dp(2) is already considered). 
- If n > 3, dp(n) = dp(n-1) + dp(n-2)

Extend: 
- if there is only 1 step each time, then dp(n) = dp(n-1) --> there is always only 1 way to climb to the top. 
- if there is three options, 1 step, 2 steps or 3 steps, then dp(n) = dp(n-1) + dp(n-2) + dp(n-3). 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n 
        
        dp = [0] * (n+1)
        dp[1] = 1 
        dp[2] = 2 
        
        for i in range(3, n+1): 
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]