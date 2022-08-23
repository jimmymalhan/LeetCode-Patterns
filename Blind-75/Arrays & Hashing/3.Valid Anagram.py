# Valid Anagram
"""
Solution Explanation::
- If the two strings are the same length, then they must be anagrams.
- Create a dictionary to store the characters and their counts
- Iterate through the first string and add the characters to the dictionary
- Iterate through the second string and subtract the characters from the dictionary
- If the dictionary is empty, then the strings are anagrams

test case1 = 'anagram', 'nagaram'
{'a': 1}
{'a': 1, 'n': 1}
{'a': 2, 'n': 1}
{'a': 2, 'n': 1, 'g': 1}
{'a': 2, 'n': 1, 'g': 1, 'r': 1}
{'a': 3, 'n': 1, 'g': 1, 'r': 1}
{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

test case2 = 'rat', 'car'
{'r': 1}
{'r': 1, 'a': 1}
{'r': 1, 'a': 1, 't': 1}
"""


class Solution:
    # O(nlogn) time and O(1) space because of the sorting of the strings where n is the length of the string
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # O(n) time and O(n) space because of the dictionary where n is the length of the string
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the length of the two strings are not equal, they cannot be anagrams
            return False
        d = {} # created once per function call
        for character in s:
            d[character] = d.get(character, 0) + 1 # get(character, 0) returns 0 if character is not in d

        for character in t:
            if character not in d: 
                return False
            d[character] -= 1 # decrement the count of c in d
            if d[character] < 0: # if the count of c in d is negative, return False
                return False
        return True


print(Solution().isAnagram("anagram", "nagaram")) # True
print(Solution().isAnagram("rat", "car")) # False
print(Solution().isAnagram2("anagram", "nagaram")) # True
print(Solution().isAnagram2("rat", "car")) # False
