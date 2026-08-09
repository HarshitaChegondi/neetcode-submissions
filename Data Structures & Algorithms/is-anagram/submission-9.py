class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        i = 0
        mydict = {}
        mydict1 = {}
        for char in s:
            mydict[char] = mydict.get(char, 0)+1 
            
        for ch in t:
            mydict1[ch] = mydict1.get(ch, 0)+1 
            
        if mydict == mydict1:
            return True
        else:
            return False
