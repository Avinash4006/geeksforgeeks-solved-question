#User function Template for python3

class Solution:
    def rotate(self, N, D):
        D%=16
        b=format(N,'016b')
        rot_left=b[D:]+b[:D]
        rot_right=b[-D:]+b[:-D]
        r_l= int(rot_left,2)
        r_r= int(rot_right,2)
        
        return r_l,r_r
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends