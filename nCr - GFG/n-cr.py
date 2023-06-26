#User function Template for python3

class Solution:
    def nCr(self, n, r):
        mod = 10**9 + 7

        # Create a dynamic programming table to store intermediate results
        dp = [[0] * (r + 1) for _ in range(n + 1)]

        # Calculate nCr using dynamic programming
        for i in range(n + 1):
            for j in range(min(i, r) + 1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

        return dp[n][r]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends