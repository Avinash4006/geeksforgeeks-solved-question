#User function Template for python3


class Solution:
    def calculate_square_sum(self, n):
        square_sum = 0
        while n > 0:
            digit = n % 10
            square_sum += digit ** 2
            n //= 10
        return square_sum

    def nextHappy(self, N):
        while True:
            N += 1
            current_number = N
            while current_number != 1 and current_number != 4:
                current_number = self.calculate_square_sum(current_number)
            if current_number == 1:
                return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends