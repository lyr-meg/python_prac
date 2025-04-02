class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-count[c], c]for c in count]
        heapq.heapify(maxheap)

        res = ""
        prev = None
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            num_left, char = heapq.heappop(maxheap)
            res+=char
            num_left+=1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if num_left<0:
                prev = [num_left, char]
           
        return res

# time complexity is O(n*logk) where n=len(s), k=unique characters (≤ 26)
# space complexity is O(n+k) because counter, maxheap is k, and res is n 