"""
26. Remove Duplicates from Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        First implementation
        """
        # i = 0
        # while i < len(nums)-1:
        #     val = nums[i]
        #     if val == nums[i+1]:
        #         nums.remove(val)
        #     else:
        #         i += 1
        # return len(nums)

        """
        Second Implementation
        """
        good_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[good_index] = nums[i]
                good_index += 1

        return good_index
