# [1. Two Sum - Easy](https://leetcode.com/problems/two-sum/)

"""
Notes:
- We are guranteed to have exactly one solution
- We don't have to worry about not finding a solution
- We don't have to worry about multiple solutions
- We are not allowed to use the same element twice
"""

from typing import List

# O(n^2) time | O(1) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# O(n) time | O(1) space
    def twoSum_HashMap(self, nums: List[int], target: int) -> List[int]:
        """
        target = 9
        currentNum = x
        x + y = 9
        y = 9 - x
        now, is there a y in the hashmap? if so, return the index of y
        """
        hashMap = {}
        for index, value in enumerate(nums):
            potentialMatch = target - value # y = 9 - x
            if potentialMatch in hashMap:
                return [hashMap[potentialMatch], index] # return the index of y
            hashMap[value] = index # x = value
        return []

print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(Solution().twoSum([3, 2, 4], 6)) # [1, 2]
print(Solution().twoSum_HashMap([2, 7, 11, 15], 9)) # [0, 1]