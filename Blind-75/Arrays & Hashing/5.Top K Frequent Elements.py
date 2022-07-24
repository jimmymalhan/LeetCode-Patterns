# Top K Frequent Elements

"""

"""

from typing import List
from collections import defaultdict
import collections
import heapq

# O(nlogn) time and O(n) space because of the dictionary where n is the length of the string
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		frequency = {}
		for num in nums:
			frequency[num] = frequency.get(num, 0) + 1
			# print(frequency)
			# {1: 1}
			# {1: 2}
			# {1: 3}
			# {1: 3, 2: 1}
			# {1: 3, 2: 2}
			# {1: 3, 2: 2, 3: 1}

			# 2nd test case:
			# {3: 1}
			# {3: 1, 0: 1}
			# {3: 1, 0: 1, 1: 1}
			# {3: 1, 0: 2, 1: 1}

					# or 
			# if num in frequency:
			# 	frequency[num] += 1
			# else:
			# 	frequency[num] = 1

		# print(frequency) # 2nd test case {3: 1, 0: 2, 1: 1}
		frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True)) # sort by value
		# print(frequency) # 2nd test case {0: 2, 3: 1, 1: 1}
		return list(frequency.keys())[:k] # return the keys of the first k elements of the dictionary # [:k] slices the dictionary to return the first k elements 



	def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
		dic = defaultdict(int)
		for num in nums:
			dic[num] += 1
		return sorted(dic, key=dic.get, reverse=True)[:k]

	def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
		dic = collections.Counter(nums)
		return [key for key, value in dic.most_common(k)]

	def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
		dic = collections.Counter(nums)
		return heapq.nlargest(k, dic, key=dic.get)

# print(Solution().topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(Solution().topKFrequent([3,0,1,0], 1)) # [0]
# print(Solution().topKFrequent2([1,1,1,2,2,3], 2)) # [1,2]
print(Solution().topKFrequent2([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent3([3,0,1,0], 1)) # [0]
# print(Solution().topKFrequent3([1,1,1,2,2,3], 2)) # [1,2]
print(Solution().topKFrequent4([3,0,1,0], 1)) # [0]