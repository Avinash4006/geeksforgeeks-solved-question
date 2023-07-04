#User function Template for python3
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        count = 0
        product = 1
        start = 0

        for end in range(n):
            product *= a[end]

            while product >= k and start <= end:
                product /= a[start]
                start += 1

            count += end - start + 1

        return count

    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends