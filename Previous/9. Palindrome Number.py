"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# Turn x into a string, and check that beginning and end of string
# are equal, up until the midpoint of the string.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        len_x = len(x_str)
        counter = 0
        half = len_x // 2
        while counter < half:
            if x_str[counter] != x_str[len_x - 1 - counter]:
                return False
            counter += 1
        return True
