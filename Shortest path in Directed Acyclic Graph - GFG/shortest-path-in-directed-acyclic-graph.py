#User function Template for python3

from typing import List

import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Initialize the distance array
        INF = float('inf')
        distances = [INF] * n
        distances[0] = 0

        # Step 2: Create the adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))

        # Step 3: Perform topological sort
        visited = [False] * n
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor, distance in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)

        dfs(0)  # Start topological sort from the source node (0)
        stack = stack[::-1]

        # Step 4: Update distances using topological order
        for node in stack:
            for neighbor, distance in graph[node]:
                if distances[node] != INF and distances[node] + distance < distances[neighbor]:
                    distances[neighbor] = distances[node] + distance

        # Check if there are unreachable vertices (distance still INF)
        for i in range(n):
            if distances[i] == INF:
                distances[i] = -1

        return distances

#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends