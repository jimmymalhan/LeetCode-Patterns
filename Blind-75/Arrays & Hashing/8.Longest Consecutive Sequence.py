# Longest Consecutive Sequence

"""
Question Explanation:
- Look at the sequence of consecutive numbers in the array and find the longest sequence of consecutive numbers.
- how to identify what is sequence? 
    - Check the start value from looking into the left neighbor
    - easiest way is to use set

Solution Explanation:
- Brute force solution: By sorting it - Time Complexity: O(nlog(n))
1. We create a set of the numbers in the array.
2. We loop through the set and check if the number - 1 is in the set.
3. If it is not, then we know that it is the beginning of a sequence.
4. We then check if the number + the length of the sequence is in the set.
5. If it is, then we know that it is the end of the sequence.
6. We then update the longest sequence if the length of the sequence is greater than the longest sequence.
7. We return the longest sequence.
"""

from typing import List  

# O(n) time | O(1) space - where n is the length of the array coz we are looping through the array once & set provides the lookup space of O(1).
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # nums.sort()
        nums = set(nums)
        longest = 0

        for num in nums:
            # Checking to see if it's the beginning of a sequence or does it have a left neighbor.
            if (num - 1) not in nums:
                length = 1
                # Checking to see if it's the end of a sequence
                while (num + length) in nums:
                    length += 1
                longest = max(longest, length)
        return longest

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9