# $$$1. Find the common elements from two lists of sorted integers, of lengths m and n, where duplicate numbers are possible.
l1 = [1, 2, 2, 2, 5, 6, 7, 8, 9]
l2 = [2, 2, 3, 3, 5, 7, 8, 9]
# What is a naive way to search? And what is its time and space complexity?
# {1:1, 2:3, 5:1, 6:1, 7:1, 8:1, 9:1}
# {2:2, 3:2, 5:1, 7:1, 8:1, 9:1}
def find_common(l1, l2):
    d1, d2 = {}, {}
    for i in l1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in l2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    res = []
    for i in d1:
        if i in d2:
            res+=[i]*min(d1[i], d2[i])
    return res
print(find_common(l1, l2))
# time complexity: O(m+n), the reason is that we have to go through both lists once to create the dictionaries.
# space complexity: O(m+n), the reason is that we have to create two dictionaries to store the counts of each number in both lists.

# How do you use the sorted property? What is its time and space complexity?  答：Use two-pointer, O(m+n) time, O(1) spatial.
def find_common2(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            res.append(l1[i])
            i+=1
            j+=1
        else:
            if l1[i] < l2[j]:
                i+=1
            else:
                j+=1
    return res
print(find_common2(l1, l2))
# time complexity is O(m+n) because we go through both lists once.
# space complexity is O(1) because we only use a few variables to store the indices and the result list.

# In what situations can binary search make it faster? 
# When One List is Much Larger:
# If the larger list (say, of size m) is extremely big compared to the smaller list (of size n), then n log m may be significantly smaller than m + n.
def upper_bound(l, target):
    left, right = 0, len(l)
    while left < right:
        mid = left + (right - left)//2
        if l[mid] <= target:
            left = mid +1
        else:
            right = mid
    return left 

def lower_bound(l, target):
    left, right = 0, len(l)
    while left < right:
        mid = left + (right - left)//2
        if l[mid] < target:
            left = mid +1
        else:
            right = mid
    return left

def find_common3(l1, l2):
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    res = []
    i = 0
    while i < len(l1):
        current = l1[i]
        l1_left = lower_bound(l1, current)
        l1_right = upper_bound(l1, current)
        l2_left = lower_bound(l2, current)
        l2_right = upper_bound(l2, current)
        res += [current] * min(l1_right - l1_left, l2_right - l2_left)
        i+=l1_right - l1_left
    return res
print(find_common3(l1, l2))
# time complexity is O(nlogm) because we go through the smaller list once and for each element we do binary search on the larger list.
# space complexity is O(1) because we only use a few variables to store the indices and the result list.


# How do you remove duplicates from the output list?
list(dict.fromkeys(res))
list(set(res))
# What are the special cases on the lengths of the two lists?
# How do you test your code? What are some of the edge cases you will test here?
# If one list is empty, return an empty result immediately.
# If one list is much smaller than the other, consider methods that iterate over the smaller list with efficient searches on the larger one.
# If both lists are similar in size or both are large, the two-pointer approach is generally effective.
# Single-Element Lists