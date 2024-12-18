"""
27. Remove Element
Easy
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Using .count() and .remove() built in methods of Python lists
        Find out how many of val exist in nums using .count, store in count
        While count > 0, call nums.remove(val)
        """

        # count = nums.count(val)
        # k = len(nums) - count
        # while count > 0:
        #     nums.remove(val)
        #     count -= 1
        # return k

        good_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[good_index] = nums[i]
                good_index += 1

        return good_index
