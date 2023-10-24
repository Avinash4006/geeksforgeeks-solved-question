#User function Template for python3

class Solution:
    def palindromicPartition(self, str):
        n = len(str)
 
        # Create two arrays to build the solution in bottom-up manner
        C = [0 for i in range(n)]
        P = [[False for i in range(n)] for i in range(n)]
 
        # Every substring with one character is a palindrome
        for i in range(n):
            P[i][i] = True
 
        # L is substring length. Build the solution in bottom-up manner by considering all substrings of length starting from 2 to n.
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1  # Set ending index
 
                # If L is 2, then we just need to compare two characters. Else need to check two corner characters and value of P[i+1][j-1]
                if L == 2:
                    P[i][j] = (str[i] == str[j])
                else:
                    P[i][j] = ((str[i] == str[j]) and P[i + 1][j - 1])
 
        # Fill table C[] in bottom up manner
        for i in range(n):
            if P[0][i]:
                C[i] = 0
            else:
                C[i] = float('inf')
                for j in range(i):
                    if P[j+1][i] and 1 + C[j] < C[i]:
                        C[i] = 1 + C[j]
 
        # Return the min cut value for complete string. i.e., str[0..n-1]
        return C[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends