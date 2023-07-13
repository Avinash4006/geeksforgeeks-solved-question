//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    bool isFrequencyUnique(int n, int arr[]) {
        std::unordered_map<int, int> frequency_map;
        std::unordered_set<int> frequency_set;

        // Count the frequency of each element in the array
        for (int i = 0; i < n; i++) {
            frequency_map[arr[i]]++;
        }

        // Check if all frequencies are unique
        for (const auto& entry : frequency_map) {
            int freq = entry.second;
            if (frequency_set.count(freq) > 0) {
                return false;
            }
            frequency_set.insert(freq);
        }

        return true;
    }
};



//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        Solution ob;
        bool ans=ob.isFrequencyUnique(n,arr);
        if(ans)
            cout<<1<<endl;
        else
            cout<<0<<endl;
    }
}
// } Driver Code Ends