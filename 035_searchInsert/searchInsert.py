from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_ = 0
        max_ = len(nums) - 1

        while min_ <= max_:
            mid_ = (min_ + max_) // 2
            if nums[mid_] == target:
                return mid_
            if nums[mid_] < target:
                min_ = mid_ + 1
            else:
                max_ = mid_ - 1
        
        return min_
