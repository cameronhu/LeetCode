"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Answers implementation. Recursive implementation starting from the center.
        Pick a center for the palindrome. The centers are either single characters
        or pairs, for a total of 2n - 1 centers (n single centers, n - 1 pair
        centers). Loop across every center, starting from 0 to len(str) - 1.
        For each center, keep adding one char to the left and to the right until the
        added characters don't equal each other or till one side reaches the end.
        If the side reaches the end of the string, return the palindromic substring
        WITHOUT the last sides added
        """

        max_palindrome = s[0]

        for i in range(len(s) - 1):
            max_palindrome = max(
                max_palindrome, find_pal(i, i, s), find_pal(i, i + 1, s), key=len
            )

        return max_palindrome


def find_pal(left_start, right_start, s):
    """
    Takes in a left starting index and right starting index for the centers of
    the palindrome. If left_start = right_start, the center is a single char and
    the palindromic sequence is odd in length. Otherwise, there is a dual center
    and the palindromic sequence is even. Add one char to the left of
    left_start, and one char to the right of right_start until those chars don't
    equal each other, or until we reach the end of the string on either end
    """
    palindromic_substring = s[left_start:right_start]

    while left_start >= 0 and right_start < len(s):
        left_char = s[left_start]
        right_char = s[right_start]
        if left_char == right_char:
            palindromic_substring = s[left_start : right_start + 1]
            left_start -= 1
            right_start += 1
        else:
            break

    return palindromic_substring

    """
    Loop implementation.

    Initialize some variable to hold our max_palindrome. Starts as s[0]

    One outer loop to start at the beginning of the string.
    For each starting point, we must also chop off the ends of the string.
    Will have a second nested loop with pointer at end of the string, and 
    decrement that pointer until the string is only 1 char or it is palindromic.
    Store any palindrome in max_palindrome if its length is > current 
    max_palindrome.
    """
    # def is_palindrome(s):
    #     for i in range(len(s)//2):
    #         if s[i] != s[len(s)- 1 - i]:
    #             return False
    #     return True

    # max_palindrome = s[0]
    # for start in range(len(s)): # Beginning of substring to check
    #     for end in range(len(s), start, -1): # End of substring to check
    #         substring = s[start : end] #Substring is the slice of s from start to end, not including end
    #         if is_palindrome(substring):
    #             max_palindrome = max(max_palindrome, substring, key = len)
    #             if len(max_palindrome) > len(s) // 2:
    #                 return max_palindrome

    # return max_palindrome

    """ Recursive implementation, terrible time complexity """
    # def is_palindrome(s):
    #     for i in range(len(s)//2):
    #         if s[i] != s[len(s)- 1 - i]:
    #             return False
    #     return True

    # def recursive_helper(s):
    #     """
    #     The recursive helper.
    #     Base case: if s is one char, return s (it is palindromic)

    #     Otherwise, check if this whole string is a palindrome.
    #     Return string if it is.
    #     If not, return the palindrome of s[1:] or s[:len(s)-1]
    #     """
    #     if len(s) == 1:
    #         return s

    #     if is_palindrome(s):
    #         return s

    #     left = recursive_helper(s[1:])
    #     right = recursive_helper(s[:len(s)-1])
    #     return max(left, right, key=len)

    # return recursive_helper(s)
