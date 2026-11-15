class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for item in strs:
            key = "".join(sorted(item))
            if key in dictionary:
                dictionary[key].append(item)
            else:
                dictionary[key] = [item]

        return list(dictionary.values())

        