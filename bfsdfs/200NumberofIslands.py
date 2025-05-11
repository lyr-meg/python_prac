class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                cur_r, cur_c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for d in directions:
                    new_r = cur_r+d[0]
                    new_c = cur_c+d[1]
                    if (0<=new_r<rows 
                        and 0<=new_c<cols 
                        and (new_r, new_c) not in visit
                        and grid[new_r][new_c]=="1"):
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    res+=1
        
        return res

# time complexity is O(N*M), why does it scan the grid twice?
# the first step scans through the grid to find the starting point of the bfs
# the second step is the bfs itself, which scans through the grid again
# space complexity is O(N*M) because everything ends up in the queue the worst case