#User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as the root
        left_child = 2 * i + 1  # Left child
        right_child = 2 * i + 2  # Right child

        # Check if the left child of the root exists and is greater than the root
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        # Check if the right child of the root exists and is greater than the root
        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            # Heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # Build a max-heap.
        # We start from the last non-leaf node and heapify all nodes in reverse order.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # Build the heap (rearrange the array)
        self.buildHeap(arr, n)

        # Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Swap
            # Call max heapify on the reduced heap
            self.heapify(arr, i, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends