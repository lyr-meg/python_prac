class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        return -1

# Time: O(logn) - We cut the search space in half each time! 
# Space: O(1) - We only use a few variables!