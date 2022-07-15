"""
Notes:

Anagrams are strings which have identical counts of characters. So anagrams, when sorted, result in the same string.

We create a dictionary and for each word in the input array, we add a key to the dictionary if the sorted version of the word doesn't already exist in the list of keys. The key then becomes the sorted version of the word, and the value for the key is an array that stores each anagram of the key. i.e. for every next word that is an anagram, we would sort the word, find the key that is equal to the sorted form, and add the original word to the list of values for the key.

- # defaultdict(list) creates a list for each key
- sorted() returns iterable. We need to join the returned list to create a string
- We can loop through dictionary to store the values in result list or we can directly use dic.values()
"""

# O(w*n*log(n)) time | O(wn) space - where w is the length of the word and n is the length of the list

from typing import List
import collections
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list) # defaultdict(list) creates a list for each key
        for s in strs:
            dic[''.join(sorted(s))].append(s) 
            # or 
            # dic[tuple(sorted(s))].append(s)

        return dic.values()


# Another way to solve is to create frozenSet out of a Counter. This way we can use frozenset as a key in a dictionary, and provides optimized time complexity without the need to sort the word.
# O(w*n) time | O(wn) space - where w is the length of the word and n is the length of the list


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            wordCounterHashKey = frozenset(Counter(word).items())
            if wordCounterHashKey not in anagrams:
                anagrams[wordCounterHashKey] = []
            anagrams[wordCounterHashKey].append(word)
        return list(anagrams.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))