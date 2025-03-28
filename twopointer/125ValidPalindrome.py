class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            l_digit = s[l]
            r_digit = s[r]
            if l_digit.isalnum() and r_digit.isalnum():
                if l_digit.lower() == r_digit.lower():
                    l+=1
                    r-=1
                else:
                    return False   
            elif not l_digit.isalnum():
                l+=1
            elif not r_digit.isalnum():
                r-=1
        
        return True