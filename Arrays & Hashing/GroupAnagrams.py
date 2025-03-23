from typing import List

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # use map to store combination of chars and strings that match
    # iterate through list and add to map
    combinationsMap = {} # List[int] : List[str]

    for str in strs:
        word = [0] * 26
        for char in str:
            charIndex = ord(char.lower()) - 97 # a = 0, b = 1, c = 2, etc...
        
            word[charIndex] += 1
        word = tuple(word)
        if word in combinationsMap:
            combinationsMap[word].append(str)
        else:
            combinationsMap[word] = [str]

    result = []
    for key in combinationsMap:
        result.append(combinationsMap[key])
    return result



print(groupAnagrams(["Eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","Eat","tea"]]
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","eat","tea"]]
