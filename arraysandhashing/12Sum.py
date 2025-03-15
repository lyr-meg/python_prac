class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            i_pair = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == i_pair:
                    return [i, j]

# time complexity: O(n^2)
# space complexity: O(1)

    def twoSum(self, nums, target):
        sum_hash = {}
        res = []
        for i in range(len(nums)):
            val = nums[i]
            if target - val in sum_hash:
                res.append(i)
                res.append(sum_hash[target - nums[i]])
                return res
            else:
                sum_hash[nums[i]] = i

# time complexity: O(n)
# space complexity: O(n)