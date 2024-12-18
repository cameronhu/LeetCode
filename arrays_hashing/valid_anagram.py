"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


"""

# Single dictionary solution


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_dict = defaultdict(int)

        for letter in s:
            count_dict[letter] += 1

        for letter in t:
            count_dict[letter] -= 1

        for value in count_dict.values():
            if value != 0:
                return False
        return True


# Two dictionary solution


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        for letter in s:
            if letter not in s_dict.keys():
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1

        for letter in t:
            if letter not in t_dict.keys():
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1

        return s_dict == t_dict
