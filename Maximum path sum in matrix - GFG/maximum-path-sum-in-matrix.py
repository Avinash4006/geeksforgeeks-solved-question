#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[0] * N for _ in range(N)]

        for c in range(N):
            dp[0][c] = Matrix[0][c]

        for r in range(1, N):
            for c in range(N):
                dp[r][c] = Matrix[r][c] + max(dp[r-1][c-1] if c > 0 else 0,
                                              dp[r-1][c],
                                              dp[r-1][c+1] if c < N-1 else 0)

        max_sum = max(dp[N-1])

        return max_sum # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends