"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

"""


# Naive Brute Force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_length = len(nums)
        for i in range(0, list_length):
            for j in range(i + 1, list_length):
                if nums[i] + nums[j] == target:
                    return [i, j]


# O(n) solution
class Solution2:
    def twoSum(self, nums, target):
        diffs = {}
        for i, value in enumerate(nums):
            if value in diffs:
                return [diffs[value], i]
            diffs[
                target - value
            ] = i  # Key is the second number needed, i is the index of the first number
