from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
# 2 1 1  2 2 1  2 2 2
# 0 1 1  0 1 1  0 2 1
# 1 0 1  1 0 1  1 0 1
# BFS
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        res = -1
        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh_oranges+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        q.append((-1, -1))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            cur_r, cur_c = q.popleft()
            if cur_r == -1:
                res+=1
                # only add (-1,-1) after a while level is processed!!
                if q:
                    q.append((-1, -1))
            else:
                for d in directions:
                    new_r, new_c = cur_r+d[0], cur_c+d[1]
                    if (0<=new_r<rows 
                        and 0<=new_c<cols 
                        and grid[new_r][new_c]==1):
                        # in dfs and bfs, need to immediate add to visit or change its value once visited
                        grid[new_r][new_c]=2
                        q.append((new_r, new_c))
                        fresh_oranges-=1

        return res if fresh_oranges==0 else -1
                        
# time complexity is O(N*M) because the first step and bfs scans through the grid twice
# space complexity is O(N*M) because everything ends up in the queue the worst case  


