#User function Template for python3
import heapq

class Solution:
    def kLargest(self, arr, n, k):
        h = arr[:k]  # Initialize a min-heap with the first K elements
        heapq.heapify(h)  # Convert the list into a min-heap

        for i in range(k, n):
            if arr[i] > h[0]:
                heapq.heapreplace(h, arr[i])  # Replace the smallest element in the heap

        l = []
        while h:
            l.append(heapq.heappop(h))  # Pop elements from the heap in ascending order

        return l[::-1]  # Reverse the list to get the elements in decreasing order


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends