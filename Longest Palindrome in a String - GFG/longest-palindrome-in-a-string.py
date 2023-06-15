#User function Template for python3

class Solution:
    def longestPalin(self, S):
        n=len(S)
        if n<=1:
            return S
        s=0
        m=1
        for i in range(n):
            l=r=i
            while r<n-1 and S[r]==S[r+1]:
                r += 1
            while l>0 and r<n-1 and S[l-1]==S[r+1]:
                l -= 1
                r += 1
            if r-l+1>m:
                m=r-l+1
                s=l
        return S[s:s+m]
        
ob=Solution()
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends