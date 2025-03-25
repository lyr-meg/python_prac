class Solution:
    def countPrimes(self, n: int) -> int:
        prime_indicator = [False]*2+[True]*(n-2)
        if n == 0 or n ==1:
            return 0
        else:
            i=2
            while i < int(sqrt(n)+1):
                if prime_indicator[i] == True:
                    mul = i
                    while i*mul < n:
                        prime_indicator[i*mul] = False
                        mul+=1
                i+=1
        return sum(prime_indicator)
    

# time complexity O(sqrt(n)log(logn)+n), The +n is from calculating the answer after the main algorithm. The sqrt(n)
# ​comes from the outer loop. Each time we hit a prime, we "cross out" the multiples of that prime because we know they aren't prime. 
#   For 2, we have to cross out n/2 numbers.
#   For 3, we have to cross out n/3 numbers.
#   For 5, we have to cross out n/5 numbers.
#   ...etc for each prime less than n.
# n/2+n/3+... This is bounded by O(loglogn) 

# space complexity O(n), for the prime_indicator array