# Find Median from Data Stream

"""
Question Explanation:
- Insert in-order - O(n)
    - Sort the numbers as we insert them in a list
    - Break the list into two halves - left and right 
    eg - [1, 2, 3, 4,] -> left = [1, 2], right = [3, 4]
    - Median = (left[-1] + right[0]) / 2 = (2 + 3) / 2 = 2.5
- Get Median - O(1)

- How to improve the time complexity of insert?
    - Use a heap to store the numbers show that we can insert in O(logn) time and moving the numbers around in the heap is O(logn) time
    eg - [1, 2, 3, 4,] -> left = [1, 2], right = [3, 4] = median = 2.5
    - We know, left <= right always 
    - small heap (MAX Heap) is left <= large heap (MIN Heap) is right
    - small heap is max heap coz we want to get the max element from the small heap. eg - [1, 2] -> 2 is the max element 
    - large heap is min heap coz we want to get the min element from the large heap. eg - [3, 4] -> 3 is the min element
    - median = (left[-1] + right[0]) / 2 = (2 + 3) / 2 = 2.5

    edge case -
    - size of small and large heap can differ by at most 1, if not, we need to balance them
    - if small heap is [1, 2, 3] and large heap is [3, 4] -> median = (3 + 3) / 2 = 3
    - if small heap is [1, 2] and large heap is [2, 3, 4] -> median = (2 + 2) / 2 = 2
    
    Workflow -
    .add(3)
    .add(2)
    .add(1)
    .add(4)
    .getMedian()

    since, we know smallHeap/MaxHeap <= largeHeap/MinHeap
    smallHeap/maxHeap | largeHeap/minHeap
    - first step - add 3 to small heap
    [3]                | []
    - second step - add 2 to small heap
    [3, 2]             | []
    By default, we add all elements to the small heap
    






Solution Explanation:
1. Create two heaps: small and large. small is a max-heap and large is a min-heap
2. If the new number is smaller than the biggest number in the small heap, add it to the small heap. Otherwise, add it to the large heap.
3. If the size of the small heap is bigger than the large heap by 2, move the top element from small to large.
4. If the size of the large heap is bigger than the small heap by 2, move the top element from large to small.
5. If the size of the large heap is bigger than the small heap by 1, the median is the top element of the large heap. Otherwise, the median is the average of the top element in the large heap and the top element in the small heap.
"""

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
