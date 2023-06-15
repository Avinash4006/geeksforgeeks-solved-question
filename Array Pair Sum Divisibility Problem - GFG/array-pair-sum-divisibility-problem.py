#User function Template for python3

class Solution:
    def canPair(self, nums, k):
 
        remainder_counts = [0] * k
        for num in nums:
            remainder = num % k
            remainder_counts[remainder] += 1

        if remainder_counts[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if remainder_counts[i] != remainder_counts[k - i]:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends