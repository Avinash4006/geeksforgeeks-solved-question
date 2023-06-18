class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        i = 1
        j = N
        turn = False
        while i != j:
            if not turn:
                i += K
                if i >= j:
                    return j
            else:
                j -= K
                if j <= i:
                    return i
            turn = not turn

        return i


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends