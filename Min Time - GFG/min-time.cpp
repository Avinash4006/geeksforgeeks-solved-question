//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    long long minTime(int n, vector<int> &locations, vector<int> &types) {
        map<int, vector<long long>> mp;
        for (int i = 0; i < n; i++) {
            if (!mp.count(types[i])) {
                mp[types[i]] = {locations[i], locations[i]};
            } else {
                mp[types[i]][0] = min(mp[types[i]][0], (long long)locations[i]);
                mp[types[i]][1] = max(mp[types[i]][1], (long long)locations[i]);
            }
        }
        vector<vector<long long>> v;
        v.push_back({0, 0});
        for (auto it : mp) {
            v.push_back(it.second);
        }
        vector<vector<long long>> dp(v.size(), vector<long long>(2, -1));
        return help(1, 0, v, dp);
    }

    long long help(int i, bool flag, vector<vector<long long>> &v, vector<vector<long long>> &dp) {
        if (i == v.size()) {
            return abs(v[i - 1][flag]);
        }
        if (dp[i][flag] != -1) {
            return dp[i][flag];
        }
        long long ans = help(i + 1, !flag, v, dp) + abs(v[i - 1][flag] - v[i][flag]);
        ans = min(ans, help(i + 1, flag, v, dp) + abs(v[i - 1][flag] - v[i][!flag]));
        return dp[i][flag] = ans + abs(v[i][0] - v[i][1]);    // code here
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        
        int n;
        cin>>n;
        
        
        vector<int> locations(n);
        for(int i=0;i<n;i++){
            cin>>locations[i];
        }
        
        
        vector<int> types(n);
        for(int i=0;i<n;i++){
            cin>>types[i];
        }
        
        Solution obj;
        long long res = obj.minTime(n, locations, types);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends