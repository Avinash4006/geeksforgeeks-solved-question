#User function Template for python3

class Solution:
    def longestKSubstr(self, s, k):
        if k <= 0:
            return -1

        char_count = {}
        left, max_length = 0, 0

        for right in range(len(s)):
            if s[right] not in char_count:
                char_count[s[right]] = 0
            char_count[s[right]] += 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            if len(char_count) == k:
                max_length = max(max_length, right - left + 1)

        if max_length == 0:
            return -1

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends