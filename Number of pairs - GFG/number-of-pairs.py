#User function Template for python3

class Solution:
    def countPairs(self, X, Y, M, N):
        Y.sort()  # Sorting array Y in non-decreasing order
        c0 = Y.count(0) 
        c1=Y.count(1)
        c2 = Y.count(2)  
        c3 = Y.count(3)  
        c4 = Y.count(4)  
        ans = 0 

        for x in X:
            if x == 0:
                continue
            elif x == 1:
                ans += c0
            elif x == 2:
                idx = self.search_l(Y, N, x)  
                if idx != -1:
                    ans += N - idx 
                ans += c0+ c1  # Adding the counts of 0s and 1s in array Y
                ans -= c3 + c4 
            else:
                idx = self.search_l(Y, N, x)  # Finding the index of the first element greater than x
                if idx != -1:
                    ans += N - idx  # Adding the count of elements after the index
                ans += c0 + c1  # Adding the counts of 0s and 1s in array Y
                if x == 3:
                    ans += c2

        return ans

    def search_l(self, Y, N, element):
        l = 0
        h = N - 1
        res = -1

        while l <= h:
            m = l + (h - l) // 2
            if Y[m] > element:
                res = m
                h = m - 1
            else:
                l = m + 1

        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        M,N=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        ob=Solution();
        print(ob.countPairs(a,b,M,N))
        #code here
# } Driver Code Ends