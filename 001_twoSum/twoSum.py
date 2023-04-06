from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            a = target - j
            if a in d:
                return [d[a], i]
            d[j] = i


class Test:
    def __init__(self):
        self.test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([4, 7, 10, 2], 6, [0, 3]),
            ([5, 10, -5], 0, [0, 2]),
        ]

    def run_tests(self):
        for nums, target, ans in self.test_cases:
            result = Solution().twoSum(nums, target)
            print(
                f"""Input: nums = {nums}, target = {target}
                Output: {result}
                Expected Output: {ans}"""
            )
            if result == ans:
                print("Correct output")
            else:
                print("Incorrect output")


Test().run_tests()
