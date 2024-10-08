# https://leetcode.com/problems/two-sum/
# Difficulty: easy

# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# You can return the answer in any order.

# Approach:
# Use dictionary to keep track of indices and elements, {element: index}
# Have other = target - nums[i] and determine if myDict contains other

class Solution(object):
    def twoSum(self, nums, target):
        myDict = {}

        for i in range(len(nums)):
            myDict[nums[i]] = i

        
        for i in range(len(nums)):
            other = target - nums[i]
            if other in myDict:
                if myDict[other] != i:
                    return [myDict[other], i]


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
        

