"""
217. Contains duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

O(n) complexity when using a set
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared_set = set()
        for i in nums:
            if i in appeared_set:
                return True
            else:
                appeared_set.add(i)
        return False
