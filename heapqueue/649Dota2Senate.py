class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_queue = collections.deque()
        d_queue = collections.deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r<d:
                r_queue.append(r+len(senate))
            elif d<r:
                d_queue.append(d+len(senate))
        
        return "Radiant" if not d_queue else "Dire"

# time complexity: O(n) because we loop through the senate string once and use deque operations which are O(1)
# space complexity: O(n) because we use two deques to store the indices of the senators