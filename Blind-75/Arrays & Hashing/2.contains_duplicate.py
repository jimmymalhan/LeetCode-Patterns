# Contains Duplicate

"""
Notes:
- If the value appears more than once, return true.
- If the value appears only once, return false.
"""

from typing import List

class Solution:
    # O(n) time | O(n) space as we are iterating through the list - n is the length of the list
    def containsDuplicate_set(self, nums: List[int]) -> bool:
        """
        A set is a collection of: 
        unordered: no duplicates
        unchangeable: no defined order
        unindexed: cannot change the items after the set has been created
        """
        seen = set() # set to store seen values
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # or 

    def containsDuplicate_short(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # O(nlogn) time | O(n) space because of the sorting of the array where n is the length of the list
    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False


print(Solution().containsDuplicate_set([1,2,3,1]))
print(Solution().containsDuplicate_sort([1,2,3,1]))
print(Solution().containsDuplicate_short([1,2,3,1]))