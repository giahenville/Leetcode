'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

def validAnagram(s: str, t: str) -> bool:
    # map out characters of strings and compare them 
    if len(s) != len(t):
        return False
    
    sMap = {}
    tMap = {}

    for char in s:
        if char in sMap:
            sMap[char] += 1
        else:
            sMap[char] = 1

    for char in t:
        if char in tMap:
            tMap[char] += 1
        else:
            tMap[char] = 1
    
    if sMap == tMap:
        return True
    else:
        return False
    
print(validAnagram("cinema", "iceman")) # True
print(validAnagram("cinem", "iceman")) # False
print(validAnagram("cinemy", "iceman")) # False
    
