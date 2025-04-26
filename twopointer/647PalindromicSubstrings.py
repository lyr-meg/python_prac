class Solution:
    def countSubstrings(self, s: str) -> int:
        # "aaaca" "a, a, a, c", "aa, aa,", "aaa"
        def check_palindrome(s):
            l, r = 0, len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        
        res = 0
        p_set = set()
        for substr_len in range(1, len(s)+1):
            for i in range(len(s)):
                if i+substr_len <= len(s):
                    substr = s[i: i+substr_len]
                    if substr in p_set:
                        res+=1
                    elif check_palindrome(substr):
                        res+=1
                        p_set.add(substr)
        
        return res

# above is brute force solution, O(n^3) time complexity

class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each char in s, treatment it as in the middle using l, r
        # expand left and right to add to result palindromes

        res = 0

        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
        
        return res

# time complexity: O(n^2) for iterating through the list and expanding around each character
# space complexity: O(1) for storing the result