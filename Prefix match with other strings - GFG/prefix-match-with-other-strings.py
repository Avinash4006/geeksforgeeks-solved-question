#User function Template for python3

class Solution:
    def klengthpref(self, arr, n, k, s):
        count = 0
        for word in arr:
            if len(word) >= k and word[:k] == s[:k]:
                count += 1
        return count

        # return list of words(str) found in the board


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends