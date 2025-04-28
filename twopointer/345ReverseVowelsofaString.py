class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #one thing to note is that a string is not changable
        l, r = 0, len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = ['*']*len(s)
        while l<=r:
            if s[l].lower() in vowels:
                lchar = s[l]
                if s[r].lower() in vowels:
                    rchar = s[r]
                    res[l] = rchar
                    res[r] = lchar
                    l+=1
                    r-=1
                else:
                    res[r] = s[r]
                    r-=1
            else:
                res[l] = s[l]
                l+=1
        
        return "".join(res)

# time complexity is O(N) because we only scan through the string once
# space complexity is O(N) because we need to store the result in a new string