# Top K Frequent Elements

"""
Question Explanation:
- From the input array, find the top k frequent elements in the array.
- You're guranteed that the answer is unique.

# Solutions Overview for [1,1,1,2,2,3]:
1 - O(nlog(n)) - Take the pairs of element from the array {1: 3, 2: 2, 3: 1}  and sort them in descending order. {3: 1, 2: 2, 1: 3}
2 - O(nlog(k)) - We can use maxHeap and add the pairs to the heap and then pop the most frequent element from the heap k times. {3: 1, 2: 2, 1: 3}
3 - O(n) Bucket sort - map the index as count to value. {3: 1, 2: 2, 1: 3}
|--------------------------------------|
|i (count) |0| 1 |  2 |  3 | 4 | 5 | 6 |
|  (value) | |[3]| [2]| [1]|   |   |   |
|----------|-|---|----|----|---|---|---|
- So, value 1 occured 3 times, value 2 occured 2 times, value 3 occured 1 time.
- Max size of the above table based on the length of the array which makes it O(n). Count of this array [1,1,1,2,2,3] is 6.
- It will be n + 1 because of the 0 index.

- Edge Case - What if we have distinct elements in the array?
If the element in the array is distinct, it can still remain O(n) time coz all the elements will fall under the same index in the table.

Solution Explanation:
1. Create an empty dictionary called frequency.
2. Loop through the nums list and for each number in the list, add 1 to the frequency dictionary.
3. Sort the frequency dictionary by value and reverse it.
4. Return the keys of the first k elements of the dictionary. 
"""

from typing import List
from collections import defaultdict, Counter
from heapq import heappush, heappop, nlargest

# O(nlogn) time and O(n) space  where n is the length of the string
# because of the hashMap O(n) space
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
		# frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True)) # sort by value
		# # print(frequency) # 2nd test case {0: 2, 3: 1, 1: 1}
		# return list(frequency.keys())[:k] # return the keys of the first k elements of the dictionary # [:k] slices the dictionary to return the first k elements 
		# # or  
		return sorted(frequency, key=frequency.get, reverse=True)[:k] # return the keys of the first k elements of the dictionary # [:k] slices the dictionary to return the first k elements

	"""
	Solution Explanation:
	1. We create a counter d which is a dictionary where the key is the item and the value is the frequency of the item.
	2. We create a heap h which is a list of tuples.
	3. We iterate through the list nums and for each item in nums, we add the item to the counter d and we add the item and its frequency to the heap h.
	4. We pop the smallest element from the heap h and append it to the result.
	5. We continue this process until the length of the heap h is less than k.
	6. We return the result.
	"""

# O(nlog(k)) time and O(k) space
	def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
		d = Counter(nums)
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
		
	# 1. We first create a hashMap, count, to store the frequency of each number in nums.
	# 2. We then create a list of lists, freq, to store the numbers with the same frequency.
	# 3. We then iterate from the highest frequency to the lowest frequency, and for each frequency, we iterate through the list of numbers with that frequency, and add them to the result list.
	# 4. If the result list has the correct length, we return the result list.

	# Bucket Sort
	# O(n) time and O(k) space
	def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
		count  = {}
		freq = [[] for i in range(len(nums) + 1)]

		for n in nums:
		# if the value of n is not in count, then set the value of n to 0, else increment the value of n by 1
			count[n] = count.get(n, 0) + 1 
		# each value that is in count is a key in freq
		for n, c in count.items():
			freq[c].append(n)
		
		return [n for c in freq[::-1] for n in c][:k]
		# or we can expand above line to:

		# res = []
		# #for i in range(len(freq) - 1, 0, -1): # reverse the list
		# for i in reversed(range(len(freq))): # reverse the list
		# 	for n in freq[i]:
		# 		res.append(n)
		# 		if len(res) == k:
		# 			return res

print(Solution().topKFrequent([3,0,1,0], 1))  # [0]
print(Solution().topKFrequent([1,1,1,2,2,3], 2))  # [1,2] or [2,1]
print(Solution().topKFrequent2([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent2([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent3([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent3([1,1,1,2,2,3], 2)) # [1,2] or [2,1]


###################### One-Liner Solutions ######################
	# """ 
	# Solution Explanation:
	# 1. Create a defaultdict to store the count of each number.
	# 2. For each number in nums, add 1 to the count of that number.
	# 3. Sort the dictionary by the count of each number.
	# 4. Return the k most frequent numbers. """

# O(nlogn) time and O(n) space  where n is the length of the string
class Solution:
	def topKFrequent5(self, nums: List[int], k: int) -> List[int]:
		dic = defaultdict(int)
		for num in nums:
			dic[num] += 1
		return sorted(dic, key=dic.get, reverse=True)[:k]

	""" 
	Solution Explanation:
	1. Create a dictionary to store the number and its frequency.
	2. Loop through the list of numbers and update the dictionary.
	3. Loop through the dictionary and return the top k numbers. """
	def topKFrequent6(self, nums: List[int], k: int) -> List[int]:
		dic = Counter(nums)
		return [key for key, value in dic.most_common(k)]

	"""
	Solution Explanation:
	1. Create a dictionary called dic.
	2. Use the Counter function to count the number of times each element appears in the list.
	3. Use the nlargest function to return the k largest elements of the dictionary.
	4. Use the key function to return the value of the dictionary. """

	def topKFrequent7(self, nums: List[int], k: int) -> List[int]:
		dic = Counter(nums)
		return nlargest(k, dic, key=dic.get) # nlargest returns the k largest elements of the iterable

print(Solution().topKFrequent5([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent5([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent6([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent6([1,1,1,2,2,3], 2)) # [1,2] or [2,1]
print(Solution().topKFrequent7([3,0,1,0], 1)) # [0]
print(Solution().topKFrequent7([1,1,1,2,2,3], 2)) # [1,2] or [2,1]