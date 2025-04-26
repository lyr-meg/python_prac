class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if not nums:
            return 0
            
        nums.sort()

        res, cur = 1, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] -1 == nums[i-1]:
                    cur+=1
                else:
                    res = max(res, cur)
                    cur = 1
        
        return max(res, cur)
    
# time complexity: O(nlogn) for sorting, O(n) for iterating through the list, so O(nlogn)
# space complexity: O(n) for storing the sorted list 