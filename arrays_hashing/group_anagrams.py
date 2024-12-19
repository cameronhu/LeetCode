"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from collections import defaultdict


# Using ordered strings as key, not tuple of counts
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = {}

        for word in strs:
            # Start as an array, convert into tuple at end
            key = "".join(sorted(word))

            if key not in anagramDict.keys():
                anagramDict[key] = [word]
            else:
                anagramDict[key].append(word)

        retList = []

        for value in anagramDict.values():
            retList.append(value)

        return retList


# O(N * M) solution, wher N is the number of words, M is the number of letters per word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a hashmap of letter counts to word key-value pairs.
        # Only loop over strs one time. For each str, generate a count tuple.
        # The tuple will be of fixed size 26, for each lowercase letter.
        # The tuple will be initialized with all 0s, and then increment each index corresponding to a letter when they appear in the string
        # Finally, return a list of the values in the letter counts dictionary

        anagramDict = defaultdict(list)

        for word in strs:
            # Start as an array, convert into tuple at end
            countList = [0] * 26

            for char in word:
                # Convert the char into an int using ord()
                # Index 0 = 'a', so ord(a)
                # Subtract ord(a) from every character
                index = ord(char) - ord("a")

                countList[index] += 1
            anagramDict[tuple(countList)].append(word)

        return list(anagramDict.values())


# O(n^2) naive implementation, timeout
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s1: str, s2: str) -> bool:
            # Function that takes in two strings and returns if they are anagrams

            if len(s1) != len(s2):
                return False

            s1_counts = defaultdict(int)
            s2_counts = defaultdict(int)

            for i in range(len(s1)):
                s1_counts[s1[i]] += 1
                s2_counts[s2[i]] += 1

            return s1_counts == s2_counts

        retList = []

        # Create a list of lists, for every word in the strs list compare to anagram lists in retList.
        # If is an anagram of one of the existing anagram lists, append to that list
        # If not, create a new list with this word and append to retList

        for word in strs:
            foundAnagram = False
            for anagramList in retList:
                if isAnagram(word, anagramList[0]):
                    anagramList.append(word)
                    foundAnagram = True
            if not foundAnagram:
                retList.append([word])

        return retList
