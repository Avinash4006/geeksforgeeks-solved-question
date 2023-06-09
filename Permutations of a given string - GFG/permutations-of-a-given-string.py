#User function Template for python3
from itertools import permutations

class Solution:
    def find_permutation(self, S):
        # Convert string to list of characters and sort them
        c = sorted(list(S))

        # Use set to store unique permutations
        u_p = set()

        # Generate permutations and add them to the set
        for p in permutations(c):
            u_p.add(''.join(p))

        # Convert set to a sorted list and return
        return sorted(u_p)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends