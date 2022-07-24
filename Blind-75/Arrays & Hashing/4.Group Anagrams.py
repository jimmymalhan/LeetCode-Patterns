# Group Anagrams

"""
Notes:

Anagrams are strings which have identical counts of characters. So anagrams, when sorted, result in the same string.

- We create a defaultdict(list) and we assign it to dic.
- We iterate through the list of strings and we create a sorted string of the characters in each word.
- We join the sorted string to create a string and append the word to the list of anagrams.
- We return the list of anagrams.
"""

# O(w*n*log(n)) time | O(wn) space - where w is the length of the word and n is the length of the list

from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) # defaultdict(list) creates a list for each key
        for word in strs:
            dic[''.join(sorted(word))].append(word) # sorted returns a list of the characters in the word and we join the list to create a string and append the word to the list of anagrams

            # or 
            # dic[tuple(sorted(s))].append(s)

        return list(dic.values())

# Another way to solve is to create frozenSet out of a Counter. This way we can use frozenset as a key in a dictionary, and provides optimized time complexity without the need to sort the word.
# The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable. Simply it freezes the iterable objects and makes them unchangeable.

# - We create a default dictionary to store the anagrams.
# - We loop through the list of words and for each word we create a hash key of the counts of each character in the word.
# - If the hash key doesn't exist in the dictionary, we create a new list for the key so we can store the anagrams.
# - We add the word to the list of anagrams.
# - We return the list of anagrams. 

# O(w*n) time | O(wn) space - where w is the length of the word and n is the length of the list.

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            wordCounterHashKey = frozenset(Counter(word).items()) # Counter(word) returns a dictionary of the counts of each character in the word
            if wordCounterHashKey not in anagrams: # if the key doesn't exist in the dictionary
                anagrams[wordCounterHashKey] = [] # create a new list for the key so we can store the anagrams
            anagrams[wordCounterHashKey].append(word) # add the word to the list of anagrams
        return list(anagrams.values()) 
        # or 
        # anagrams = defaultdict(list)
        # for word in strs:
        #     anagrams[frozenset(Counter(word).items())].append(word)
        # return list(anagrams.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))