"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # c = Counter(nums)
        # return len(list(c)) != len(nums)

        elements = set()

        for element in nums:
            if element not in elements:
                elements.add(element)
            elif element in elements:
                return True
        return False
