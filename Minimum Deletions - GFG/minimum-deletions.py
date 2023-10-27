#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self, S):
        n = len(S)
        # Create a 2D array to store the minimum deletions needed for substrings.
        dp = [[0] * n for _ in range(n)]

        # Initialize the dp array for substrings of length 1.
        for i in range(n):
            dp[i][i] = 0

        # Fill the dp array for substrings of length 2 and above.
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        # The minimum deletions needed to make the entire string a palindrome is stored in dp[0][n-1].
        return dp[0][n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends