#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        xor_sum = 0
        for bit in range(32):
            # Count the number of elements with the current bit set (1) and the number of elements with it unset (0).
            count_set_bit = sum(((arr[i] >> bit) & 1) for i in range(n))
            count_unset_bit = n - count_set_bit
            # For each bit position, calculate the contribution to the XOR sum.
            # Each set bit contributes count_set_bit * count_unset_bit pairs.
            xor_sum += (count_set_bit * count_unset_bit) * (1 << bit)
        return xor_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends