"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Find the maximum value of the array, store as the max subarray
        # Start from the beginning of the array, keep a running subtotal of the subarray
        # Check if adding a[i] will make the subarray larger than just a[i]
        # If not, make subarray just a[i]. Else, add a[i].
        # Check if subarray is greater than the max. If true, reassign the max. Increment i.

        # max_val = max(nums)
        # i = 1
        # subarray_val = nums[0]
        # while i < len(nums):
        #     curr_val = nums[i]
        #     if curr_val + subarray_val > curr_val:
        #         subarray_val += curr_val
        #     else:
        #         subarray_val = curr_val
        #     if subarray_val > max_val:
        #         max_val = subarray_val
        #     i += 1
        # return max_val

        max_val = max(nums)
        subarray_val = nums[0]

        i = 1
        while i < len(nums):
            curr_val = nums[i]
            subarray_val = max(curr_val, subarray_val + curr_val)
            max_val = max(subarray_val, max_val)
            i += 1

        return max_val
