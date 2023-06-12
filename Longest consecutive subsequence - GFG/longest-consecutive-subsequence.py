 #User function Template for python3
class Solution:
    
    def findLongestConseqSubseq(self,arr, N):
        
        s = set()
        a = 0
        for e in arr:
            s.add(e)
        for i in range(N):
            if (arr[i]-1) not in s:
                j = arr[i]
                while(j in s):
                    j += 1
                a = max(a, j-arr[i])
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends