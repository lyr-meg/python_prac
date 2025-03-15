class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # here is the key to avoid duplicates
            # if the current number is the same as the previous one, skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # here is the key to avoid duplicates
                    # if the current number is the same as the previous one, skip it
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
        return res
    

# time complexity: O(n^2+nlogn)
# space complexity: O(1) or O(n) if sort consumes space