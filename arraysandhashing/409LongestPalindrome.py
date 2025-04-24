class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        for i in c.values():
            res += (i//2)*2
        
        if res == len(s):
            return res
        else:
            return res+1

# time complexity: O(n) where n is the length of the string because we are iterating through the string once to count the frequency of each 
# character and then iterating through the frequency dictionary to calculate the result.
# space complexity: O(1) because the frequency dictionary will have at most 26 characters (lowercase English letters) so it is constant space.
