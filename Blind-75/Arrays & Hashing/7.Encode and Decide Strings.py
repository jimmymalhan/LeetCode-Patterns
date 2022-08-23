# Encode and Decode Strings

# Question:
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

"""
Notes:
- Premium 'leetcode' problem solving on 'lintcode'.
-  It's a Design Algorithm to encode input to a string and decode the string to the original input.
- We can have any possible input but not just lowercase input. 
- We need to focus on creating a delimiter '#' to separate the strings that means how find where the string ends and where the next string starts.

- Edge case input:
     "leet", "co#de", output would be leet#co#de. When we split the string; it's 3 strings which is not the same as the input.
AND we can't store the count of the characters for each string in separate data structure it needs be stateless.
eg: "leet", "co#de",counts are [4, 5]. We can't store [4, 5] in a separate data structure to refer.

- Solution:
- We can store it in the string of the input. So, Read the count of each character in the input, add a delimiter between the count and the character. It will only read the count of the character after the delimiter '#'.
- Even if we have delimiter '#' and integer in the input. We can still read the count of the character after the assigned delimiter '#'.
eg: input: "leet", "#eet", "##et", "#ee6".
- We will read the count of the characters in strings ONLY after the assigned delimiter '#'. 
eg: 4#"leet", 4#"#eet", 4#"##et", 4#"#ee6".
"""

from typing import List  

# O(n) time and O(n) space
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = "" # we need return a single string
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    1. We initialize the result array and the pointer i to 0.
    2. We loop through the string and whenever we encounter a # we know that we have reached the end of a string.
    3. We extract the length of the string from the string from i to j and convert it to an integer.
    4. We append the string to the result array and increment the pointer i by 1+length.
    5. We return the result array. 
    """

    def decode(self, str):
        res, i = [], 0 # i is pointer to the current index of the string to reach char by char

        while i < len(str):
            j = i # j is another pointer
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # length is the count of the characters in the string
            res.append(str[j+1:j+1+length]) 
            i = j+1+length # i is the pointer to the next string or end of the string
        return res

print(Solution().encode(["lint","code","love","you"]))
print(Solution().decode("4#lint4#code4#love3#you"))
