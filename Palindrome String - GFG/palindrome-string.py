#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    S=S.lower()
	    S=''.join((filter(str.isalnum, S)))
	    return int(S==S[::-1])
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends