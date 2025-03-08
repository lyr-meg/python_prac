class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for n in nums:
            if n in unique:
                return True
            else:
                unique.add(n)
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)