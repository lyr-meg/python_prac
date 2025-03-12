class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_nums = Counter(nums)
        c_nums_list = [[-c_nums[n], n] for n in c_nums]
        heapq.heapify(c_nums_list)
        output = []
        while k>0:
            count, num= heapq.heappop(c_nums_list)
            output.append(num)
            k-=1
        return output

# Using a hash map allows us to count occurrences in O(n)
# Using a heap allows us to find the top k elements in O(k log n)
# Overall time complexity is O(n + k log n)
# Space complexity is O(n) for the hash map and O(k) for the heap

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
# time complexity is O(n)
# backet sort method