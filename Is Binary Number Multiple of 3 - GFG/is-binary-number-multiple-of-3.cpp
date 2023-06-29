//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution {
public:
    int isDivisible(string s) {
        int n = s.length();
        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            int bit = s[i] - '0';
            if (bit == 1) {
                if (i % 2 == 0) {
                    sum += 1;
                } else {
                    sum -= 1;
                }
            }
        }
        return (sum % 3 == 0) ? 1 : 0;
    }
};



//{ Driver Code Starts.
int main(){
    
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        Solution ob;
        cout << ob.isDivisible(s) << endl;
    }
return 0;
}


// } Driver Code Ends