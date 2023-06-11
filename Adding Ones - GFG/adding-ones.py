#User function Template for python3

class Solution:
    def update(self, a, n, updates, k):
        for i in range(k):
            updates[i] -= 1

        p_s = [0] * n

        for i in range(k):
            p_s[updates[i]] += 1

        c_s = 0

        for i in range(n):
            c_s += p_s[i]
            a[i] += c_s

        return a



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n , k = sz[0] , sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.update(a, n, updates, k)
        print(*a)

        T -= 1


# } Driver Code Ends