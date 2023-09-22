#User function Template for python3

class Solution:
    def find(self, arr, n, x):
        # Initialize variables to store the first and last occurrences
        f_occ = -1
        l_occ = -1

        # Binary search for the first occurrence
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                f_occ = mid
                r = mid - 1  # Continue searching on the left side
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        # Reset left and right for the binary search for the last occurrence
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                l_occ = mid
                l = mid + 1  # Continue searching on the right side
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        return (f_occ, l_occ)


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends