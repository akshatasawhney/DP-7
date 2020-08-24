"""
// Time Complexity : o(m*n)
// Space Complexity : o(m*n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word2)
        m = len(word1)
        
        dp = [[0 for i in range(m + 1)] for j in range( n + 1)] #creating dp matrix
        
        for i in range(len(dp)):
            dp[i][0] = i
            
        for i in range(len(dp[0])):
            dp[0][i] = i
            
     
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word2[i - 1] == word1[j - 1]: #if chars at current positions in word1 and word2 are the same, simply get the value diagonally above
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 #else, find the min val out of the three neighbours and add 1
                    
        return dp[n][m]