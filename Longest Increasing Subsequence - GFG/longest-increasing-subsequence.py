#User function Template for python3

class Solution:
    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        if n == 0:
            return 0

        piles = []  # Stores the top element of each pile
        for num in a:
            idx = self.bisect_left(piles, num)  # Find the insertion point using binary search
            if idx == len(piles):
                piles.append(num)
            else:
                piles[idx] = num  # Replace the top element of a pile

        return len(piles)

    # Custom implementation of bisect_left for binary search
    def bisect_left(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends