#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        count = 0

        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                count += 1
                if count == k:
                    return a[top][i]
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                count += 1
                if count == k:
                    return a[i][right]
            right -= 1

            # Traverse bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    count += 1
                    if count == k:
                        return a[bottom][i]
                bottom -= 1

            # Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    count += 1
                    if count == k:
                        return a[i][left]
                left += 1

        return None


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends