#User function Template for python3

class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # Initialize an array to keep track of visited vertices.
        visited = [False] * V
        
        # Initialize the result list to store the DFS traversal.
        result = []

        # Helper function for DFS traversal starting from a specific vertex.
        def dfs(vertex):
            # Mark the current vertex as visited.
            visited[vertex] = True
            # Append the current vertex to the result list.
            result.append(vertex)
            # Traverse all adjacent vertices that are not visited yet.
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Start DFS from the 0th vertex (assuming 0-indexed vertices).
        dfs(0)

        return result



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends