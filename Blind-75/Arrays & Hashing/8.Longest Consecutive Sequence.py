# Longest Consecutive Sequence

"""
Question Explanation:

Solution Explanation:
1. We create a set of the numbers in the array.
2. We loop through the set and check if the number - 1 is in the set.
3. If it is not, then we know that it is the beginning of a sequence.
4. We then check if the number + the length of the sequence is in the set.
5. If it is, then we know that it is the end of the sequence.
6. We then update the longest sequence if the length of the sequence is greater than the longest sequence.
7. We return the longest sequence.
"""

from typing import List  

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Checking to see if it's the beginning of a sequence
            if (num - 1) not in numSet:
                length = 1
                # Checking to see if it's the end of a sequence
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))