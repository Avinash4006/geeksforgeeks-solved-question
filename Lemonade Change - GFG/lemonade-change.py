#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        bill5 = 0
        bill10 = 0

        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10:
                if bill5 == 0:
                    return False
                bill5 -= 1
                bill10 += 1
            elif bill == 20:
                if bill10 >= 1 and bill5 >= 1:
                    bill10 -= 1
                    bill5 -= 1
                elif bill5 >= 3:
                    bill5 -= 3
                else:
                    return False

        return True

        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends