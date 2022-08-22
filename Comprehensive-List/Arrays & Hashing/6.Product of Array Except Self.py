# Product of Array Except Self
"""
Question explanation:
Input - 1,2,3,4
for 1st element -  2 * 3 * 4 = 24
for 2nd element -  1 * 3 * 4 = 12
for 3rd element -  1 * 2 * 4 = 8
for 4th element -  1 * 2 * 3 = 6

Output- 24,12,8,6
"""


from typing import List
"""
1. We initialize an array of length len(nums) with all 1s.
2. We initialize a leftRunningProduct to 1 and a rightRunningProduct to 1.
3. We loop through the array from left to right.
    a. We update the products[i] to the current leftRunningProduct.
    b. We update the leftRunningProduct to the current leftRunningProduct multiplied by the current number.
4. We loop through the array from right to left.
    a. We update the products[i] to the current rightRunningProduct.
    b. We update the rightRunningProduct to the current rightRunningProduct multiplied by the current number.
5. We return the products array.
"""

class Solution:
# O(n) time and O(n) space coz separate array for storing the product of all the numbers to the left of the current number and the product of all the numbers to the right of the current number
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        
        leftRunningProduct = 1
        for i in range(len(nums)):
            products[i] = leftRunningProduct 
            leftRunningProduct *= nums[i]
            
        rightRunningProduct = 1
        for i in reversed(range(len(nums))):
            products[i] *= rightRunningProduct # products[i] multiplies by the current number
            rightRunningProduct *= nums[i] 
            
        return products


# O(n) time and O(1) space coz we can use the output array to store the product of all the numbers to the left of the current number and the product of all the numbers to the right of the current number

# 1. We firstly initialize the result list with 1s.
# 2. We then calculate the product of all the numbers in the list.
# 3. We then multiply the product by each number in the list.
# 4. We then multiply each number in the list by the product.
# 5. We then return the result.
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        res = []
        
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i] # p multiplies by the current number
        
        p = 1
        for i in reversed(range(len(nums))):
        #for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * p  # res[i] multiplies by the current number
            p = p*nums[i] # p multiplies by the current number
        
        return res

print(Solution().productExceptSelf1([1,2,3,4])) # [24,12,8,6]
print(Solution().productExceptSelf2([1,2,3,4])) # [24,12,8,6]

