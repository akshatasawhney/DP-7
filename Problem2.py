"""
// Time Complexity : o(m*n)
// Space Complexity : o(m*n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl = len(s)
        pl = len(p)
        
        dp = [[False for i in range (pl + 1)] for j in range(sl + 1)]
        
        dp[0][0] = True
        
        for i in range(1,len(dp[0])):
            if p[i-1] == "*": #if current char is a *, we go back two characters to check if string till that point is possible or not
                dp[0][i] = dp[0][i - 2]
                
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if p[j-1] != "*":
                    if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                        dp[i][j] = dp[i-1][j-1]

                else: #if we are at a *, there will be two cases
                    #zero case, dont consider the character at all
                    dp[i][j] = dp[i][j - 2]
                    
                    #one case
                    if j > 1 and p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        if dp[i - 1][j]:
                            dp[i][j]  = True
              
        return dp[-1][-1]
            