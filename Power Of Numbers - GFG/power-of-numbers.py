#User function Template for python3

class Solution:
    def power(self, N, R):
        mod = 10**9 + 7

        # Recursive helper function for modular exponentiation
        def pow_helper(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                half = pow_helper(base, exponent // 2)
                return (half * half) % mod
            else:
                half = pow_helper(base, (exponent - 1) // 2)
                return (base * half * half) % mod

        # Call the helper function to calculate the power modulo mod
        result = pow_helper(N, R)

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends