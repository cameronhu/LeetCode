"""13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


# Cleaned up the second implementation using a for loop
class Solution:
    def romanToInt(self, s: str) -> int:
        conv_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return_int = 0

        for i in range(len(s)):
            curr_num = conv_dict[s[i]]
            if i < (len(s) - 1) and curr_num < conv_dict[s[i + 1]]:
                return_int -= curr_num
            else:
                return_int += curr_num
        return return_int


# Second Implementaion
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         conv_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
#         return_int = 0
#         i = 0
#         while i < len(s) - 1:
#             curr_num = conv_dict[s[i]]
#             next_num = conv_dict[s[i+ 1]]
#             if curr_num < next_num:
#                 return_int += next_num - curr_num
#                 i += 2
#             else:
#                 return_int += curr_num
#                 i += 1
#         if i != len(s):
#             return_int += conv_dict[s[i]]
#         return return_int

# First implementation
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         conv_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
#         return_int = 0
#         while len(s) > 1:
#             print(s)
#             numeral = s[0]
#             next_num = s[1]
#             print(f"Numeral is {numeral} and next_num is {next_num}")
#             if numeral == 'I' and (next_num == 'V' or next_num == 'X'):
#                 if next_num == 'V':
#                     return_int += 4
#                 else:
#                     return_int += 9
#                 s = s[2:]
#             elif numeral == 'X' and (next_num == 'L' or next_num == 'C'):
#                 if next_num == 'L':
#                     return_int += 40
#                 else:
#                     return_int += 90
#                 s = s[2:]
#             elif numeral == 'C' and (next_num == 'D' or next_num == 'M'):
#                 if next_num == 'D':
#                     return_int += 400
#                 else:
#                     return_int += 900
#                 s = s[2:]
#             else:
#                 print(f"Conv_dict[{numeral}] is {conv_dict[numeral]}")
#                 return_int += conv_dict[numeral]
#                 s = s[1:]
#             print(return_int)
#         if len(s) != 0:
#             return_int += conv_dict[s]
#         return return_int
