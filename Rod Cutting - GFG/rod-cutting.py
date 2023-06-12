#User function Template for python3
class Solution:
    def cutRod(self, price, n):
        v = [0 for x in range(n + 1)]
        for i in range(1, n + 1):
            m_v = float('-inf')
            for j in range(i):
                m_v = max(m_v, price[j] + v[i - j - 1])
            v[i] = m_v
        return v[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends