class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        
        def dfs(i):
            visited.add(i)
            for j in rooms[i]:
                if j not in visited:
                    dfs(j)
        
        dfs(0)
        
        return len(visited) == len(rooms)


# time complexity: O(n) because we visit each room once
# space complexity: O(n) for the visited set 