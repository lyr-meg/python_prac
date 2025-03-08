
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """       
        d = {}

        for i in arr:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        return len(list(set(d.values())))==len(d.values())

# Time complexity:
# O(n) where n denotes the number of elements in an array as we're looping through each of them.

# Space complexity:
# O(n) because we're storing them in a hashset whose length is dependent on the number of elemts like 'n' number of elements may take up 'n' amount of space

#using counter, less efficient
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """  
        counter_arr = Counter(arr)
        keys = []
        for c in counter_arr:
            keys.append(counter_arr[c])
        
        keys_unique = len(list(set(keys)))
        keys_len = len(keys)
        return keys_unique == keys_len

def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        freq = set()
        for num in counter:
            if counter[num] in freq:
                return False
            else:
                freq.add(counter[num])
        return True