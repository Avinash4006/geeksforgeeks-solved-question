//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// design the class in the most optimal way

#include <unordered_map>

class LRUCache
{
private:
    int capacity;
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    list<int> recentlyUsed;

public:
    LRUCache(int cap)
    {
        capacity = cap;
    }

    int GET(int key)
    {
        if (cache.find(key) != cache.end())
        {
            // Move the key to the front of the recentlyUsed list
            recentlyUsed.erase(cache[key].second);
            recentlyUsed.push_front(key);
            cache[key].second = recentlyUsed.begin();
            return cache[key].first;
        }
        return -1;
    }

    void SET(int key, int value)
    {
        if (cache.find(key) != cache.end())
        {
            // Update the value of the existing key
            cache[key].first = value;
            // Move the key to the front of the recentlyUsed list
            recentlyUsed.erase(cache[key].second);
            recentlyUsed.push_front(key);
            cache[key].second = recentlyUsed.begin();
        }
        else
        {
            if (cache.size() == capacity)
            {
                // Remove the least recently used key from cache
                int leastUsedKey = recentlyUsed.back();
                cache.erase(leastUsedKey);
                recentlyUsed.pop_back();
            }
            // Add the new key to cache and the front of the recentlyUsed list
            recentlyUsed.push_front(key);
            cache[key] = make_pair(value, recentlyUsed.begin());
        }
    }
};



//{ Driver Code Starts.

int main()
{
    int t;
    cin >> t;
    while (t--)
    {

        int capacity;
        cin >> capacity;
        LRUCache *cache = new LRUCache(capacity);
        
        int queries;
        cin >> queries;
        while (queries--)
        {
            string q;
            cin >> q;
            if (q == "SET")
            {
                int key;
                cin >> key;
                int value;
                cin >> value;
                cache->SET(key, value);
            }
            else
            {
                int key;
                cin >> key;
                cout << cache->GET(key) << " ";
            }
        }
        cout << endl;
    }
    return 0;
}

// } Driver Code Ends