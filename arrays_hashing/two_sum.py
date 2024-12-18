"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# Single dictionary implementation, O(n) complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements_dict = {}

        for index in range(len(nums)):
            num = nums[index]

            if num in complements_dict.keys():
                return [complements_dict[num], index]

            complements_dict[target - num] = index


# Brute Force O(n^2) complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
