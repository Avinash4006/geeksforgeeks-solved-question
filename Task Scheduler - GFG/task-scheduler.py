#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        freq = [0] * 26  
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort(reverse=True)  

        max_freq = freq[0] 
        idle_time = (max_freq - 1) * K 

        for f in freq[1:]:
            idle_time -= min(f, max_freq - 1)  

        idle_time = max(0, idle_time) 

        return N + idle_time

        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends