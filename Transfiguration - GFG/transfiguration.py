#User function Template for python3

class Solution:
    def transfigure(self, A, B):
        if len(A) != len(B):
            return -1
        
        count = [0] * 256  
        
        for i in range(len(A)):
            count[ord(A[i])] += 1
            count[ord(B[i])] -= 1
        
        for i in range(256):
            if count[i] != 0:  
                return -1
        
        i = len(A) - 1
        j = len(B) - 1
        transformations = 0
        
        while i >= 0 and j >= 0:
            if A[i] != B[j]:
                transformations += 1
            else:
                j -= 1
            i -= 1
        
        return transformations


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends