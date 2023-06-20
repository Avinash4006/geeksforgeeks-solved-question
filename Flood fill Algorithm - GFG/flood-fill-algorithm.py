class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return image

        startColor = image[sr][sc]

        def floodFillDFS(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != startColor:
                return

            image[row][col] = newColor

            floodFillDFS(row + 1, col)
            floodFillDFS(row - 1, col)
            floodFillDFS(row, col + 1)
            floodFillDFS(row, col - 1)

        floodFillDFS(sr, sc)
        return image



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends