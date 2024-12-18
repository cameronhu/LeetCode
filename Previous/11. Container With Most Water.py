# 11. Container With Most Water

# Companies
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Given height of i and height of j, if h[i] <= h[j], then any box with an
        area greater than h[i] * (j - i) must be contained within the subarray
        from [i + 1, to j]. This is because h[i] is < h[j], meaning the height of
        the box is guaranteed to be defined by h[i] (h[i] is the max of the box). 
        If we were to move j to j-1, the max height would still be h[i], but the max
        width would now be j - 1 - i, meaning the max box area cannot be bigger 
        than from our original subarray (from [i to j]). Therefore, in the case that
        h[i] <= h[j] for some max_area, if a bigger area exists, it must be within
        the subarray h[i+1 : j+1]. Likewise, if h[j] <= h[i], we decrement j because
        the max area must be within some subarray [i to j 01]
        """
        
        i = 0
        j = len(height) - 1
        max_area = 0 
        while i != j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1
        
        return max_area
        
        """
        Calculate a largest area from the furthest index from i, starting from
        i = 0. Once a max has been found, there are certain values for the height[i]
        that no longer can produce a greater area, given len(list) - i as the
        width of the box. 

        For example, say the max_area is found to be 49, and we are at i = 1 with
        a list length of 9. Max x is len(list) - i = 8. The height[i] must therefore
        be at least max_area // (len(list) - i) + 1, or 49 // 8 + 1 = 7. 8*7 = 56.
        If height[i] is < this value, skip the nested for loop because all possible
        area values will not be greater than max
        """

        # max_area = 0
        # list_length = len(height)

        # for i in range(list_length):
        #     i_height = height[i]
        #     height_needed = 1 + max_area // (list_length - i)

        #     if i_height >= height_needed:
        #         j = list_length - 1
        #         while j > i and ((j - i) * i_height >= max_area):
        #             j_height = height[j]
        #             this_area = min(i_height, j_height) * (j - i)
        #             max_area = max(max_area, this_area)
        #             j -= 1

        # return max_area

        """
        Starting from i = 0, find height[i]. Find greatest index where 
        height[index] >= height[i]. Calculate that area: height[i] * (index - i)
        Store max area in a variable. If this area > max_area, replace. Return 
        max_area
        """

        """
        Brute force nested for loops, O(n^2) time complexity.
        """

        # max_area = 0
        # list_length = len(height)

        # for i in range(list_length):
        #     i_height = height[i]

        #     for j in range(list_length - 1, i, -1):
        #         j_height = height[j]
        #         this_area = min(i_height, j_height) * (j - i)
        #         max_area = max(max_area, this_area)
        
        # return max_area
