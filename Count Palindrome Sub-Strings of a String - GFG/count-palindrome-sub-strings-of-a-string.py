#User function Template for python3

class Solution:
    def CountPS(self, S, N):
        count = 0

        # Helper function to expand around the center
        def expand_around_center(left, right):
            nonlocal count
            while left >= 0 and right < N and S[left] == S[right]:
                # Found a palindromic substring
                count += 1
                left -= 1
                right += 1

        # Iterate through each character as the potential center
        for i in range(N):
            # Expand around the center for odd-length palindromes
            expand_around_center(i, i)

            # Expand around the center for even-length palindromes
            expand_around_center(i, i + 1)

        return count - N  # Subtract N to exclude single-character palindromes




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.CountPS(S,N))
# } Driver Code Ends