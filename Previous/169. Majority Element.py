"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        First implementation utilizes the Counter data structure
        """
        # c = Counter(nums)
        # return c.most_common(1)[0][0]

        """
        Second implementation uses loops and dictionaries
        """
        counts = {}

        for i in range(len(nums)):
            element = nums[i]
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1
        return max(counts, key=counts.get)
