# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        check = 999
        while check != 0:
            num = (l+r)/2
            check = guess((l+r)/2)
            if check == 1:
                l = num+1
            if check == -1:
                r = num-1         
        return num

def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            g = l+(r-l)/2
            if guess(g) > 0:
                l = g+1
            elif guess(g) < 0:
                r = g-1
            else:
                return g

# - Time Complexity: O(logn)
# - Space Complexity: O(1)