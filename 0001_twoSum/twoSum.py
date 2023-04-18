from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            a = target - j
            if a in d:
                return [d[a], i]
            d[j] = i


# Pseudocode:
# create an empty dictionary
# loop through nums list: keep track of i (0-n) and j (0-n values)
#   calculate remainder a: target - value
#   if a is in dict:
#       return array of [a value, current index i]
#   if not in array, append value(key) and index (value) into dict
