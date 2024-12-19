"""
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""


# Using two pointers. First pointer is to the position to edit in the list, second pointer is iterating across all values of the list.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Two pointers
        # First pointer is to the next position in the array we wish to evaluate sorting for
        # Second pointer is a pointer across all values of the original array

        sortPtr = 1
        unique_nums = len(nums)
        for iteratorPtr in range(1, len(nums)):
            if nums[iteratorPtr] != nums[iteratorPtr - 1]:
                nums[sortPtr] = nums[iteratorPtr]
                sortPtr += 1
            else:
                # Can do without unique_nums: the sortPtr is already counting the number of unique numbers
                unique_nums -= 1

        return unique_nums


# Using pop, O(n * M), where M is the number of values to shift after popping
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # For each number in nums, check the value next to it
        # If the value next to it is the same, then remove that item using .pop
        # k will be initialized as the length of the list. For every pop, decrement k
        # Go to the second to the last value in the list

        ptr: int = 0
        unique_nums: int = len(nums)

        for i in range(len(nums) - 1):

            # Check the next member
            thisValue = nums[ptr]
            nextValue = nums[ptr + 1]

            if thisValue == nextValue:
                nums.pop(ptr + 1)
                unique_nums -= 1
            else:
                ptr += 1

        return unique_nums
