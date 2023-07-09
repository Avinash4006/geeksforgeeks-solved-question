//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    // Function to find the smallest positive number missing from the array.
    int missingNumber(int arr[], int n) 
    { 
        // Separate positive integers from the array and ignore non-positive integers (including 0).
        int posArr[n];
        int posSize = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > 0) {
                posArr[posSize++] = arr[i];
            }
        }

        // Mark visited elements.
        for (int i = 0; i < posSize; i++) {
            int num = abs(posArr[i]);
            if (num <= posSize) {
                posArr[num - 1] = -abs(posArr[num - 1]);
            }
        }

        // Find the first positive number which is not marked as visited.
        for (int i = 0; i < posSize; i++) {
            if (posArr[i] > 0) {
                return i + 1;
            }
        }

        // All positive numbers from 1 to posSize are present, so return posSize + 1.
        return posSize + 1;
    }
};


//{ Driver Code Starts.

int missingNumber(int arr[], int n);

int main() { 
    
    //taking testcases
    int t;
    cin>>t;
    while(t--){
        
        //input number n
        int n;
        cin>>n;
        int arr[n];
        
        //adding elements to the array
        for(int i=0; i<n; i++)cin>>arr[i];
        
        Solution ob;
        //calling missingNumber()
        cout<<ob.missingNumber(arr, n)<<endl;
    }
    return 0; 
} 
// } Driver Code Ends