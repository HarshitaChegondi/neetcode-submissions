class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictAnagram = {}
        for s in strs:
            key = "".join(sorted(s))
            if len(s) != len(dictAnagram.keys()):
                dictAnagram.setdefault(key, []).append(s)
            elif len(s) == len(dictAnagram.keys()):
                dictAnagram.setdefault(key, []).append(s)
        return list(dictAnagram.values())