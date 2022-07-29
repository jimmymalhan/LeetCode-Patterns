# Top K Frequent Elements

"""

"""

from typing import List
from collections import defaultdict, Counter
from heapq import heappush, heappop, nlargest

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


	""" 
	1. Create a defaultdict to store the count of each number.
	2. For each number in nums, add 1 to the count of that number.
	3. Sort the dictionary by the count of each number.
	4. Return the k most frequent numbers. """
	def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
		dic = defaultdict(int)
		for num in nums:
			dic[num] += 1
		return sorted(dic, key=dic.get, reverse=True)[:k]
	""" 
	1. Create a dictionary to store the number and its frequency.
	2. Loop through the list of numbers and update the dictionary.
	3. Loop through the dictionary and return the top k numbers. """
	def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
		dic = Counter(nums)
		return [key for key, value in dic.most_common(k)]
	"""
	1. Create a dictionary called dic.
	2. Use the Counter function to count the number of times each element appears in the list.
	3. Use the nlargest function to return the k largest elements of the dictionary.
	4. Use the key function to return the value of the dictionary. """

	def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
		dic = Counter(nums)
		return nlargest(k, dic, key=dic.get) # nlargest returns the k largest elements of the iterable
	
	# O(NlogN) time and O(N) space
	def topKFrequent5(self, nums: List[int], k: int) -> List[int]:
		if not nums:
			return []

		if len(nums) == 1:
			return nums[0]

		# first find freq - freq dict
		d = {}
		for num in nums:
			if num in d:
				d[num] -= 1 # reverse the sign on the freq for the heap's sake # why do we need to reverse the sign? because the heap is a min heap and we want the largest element to become the smallest element
			else:
				d[num] = -1

		h = []
		for key in d:
			heappush(h, (d[key], key)) # (freq, item) - O(log(N))

		res = []
		count = 0
		while count < k: # while the count is less than k, keep popping the smallest element
			frq, item = heappop(h) # heappop returns the smallest element of the heap h and removes it from h - O(log(N))
			res.append(item) # append the smallest element to the result
			count += 1
		return res
	"""
	1. We create a counter d which is a dictionary where the key is the item and the value is the frequency of the item.
	2. We create a heap h which is a list of tuples.
	3. We iterate through the list nums and for each item in nums, we add the item to the counter d and we add the item and its frequency to the heap h.
	4. We pop the smallest element from the heap h and append it to the result.
	5. We continue this process until the length of the heap h is less than k.
	6. We return the result.
	"""
# O(nlog(k)) time and O(k) space
	def topKFrequent6(self, nums: List[int], k: int) -> List[int]:
		if len(nums) == 1:
			return [nums[0]]
		
		d = Counter(nums)
		# insert k items into heap O(nlog(k))
		h = []

		for key in d: # O(N)
			heappush(h, (d[key], key)) # freq, item - O(log(k)) # h is a heap to insert (freq, item) into h, d[key] is the frequency of the item, key is the item - O(log(k)) 
			if len(h) > k: # if the length of h is greater than k, then pop the smallest element 
				heappop(h) 

		res = []
		while h: 
			frq, item = heappop(h) # heappop returns the smallest element of the heap h and removes it from h - O(log(k))
			res.append(item) # append the item to the result - O(1)
		return res

print(Solution().topKFrequent([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent2([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent2([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent3([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent3([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent4([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent4([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent5([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent5([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent6([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent6([1,1,1,2,2,3], 2)) # [1,2] or [2,1]