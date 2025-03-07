# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l<r:
            mid = l+(r-l)//2
            call_return = isBadVersion(mid)
            if call_return:
                r = mid
            else:
                l = mid+1
        return l

# space complexity: O(1)
# time complexity: O(log n)