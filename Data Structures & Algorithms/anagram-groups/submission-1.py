class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        subres = []
        visited = set()

        for str in strs:
            if str not in visited:
                subres = []
                for w in strs:
                    if len(str) == len(w) and sorted(str) == sorted(w):
                        subres.append(w)
                        visited.add(w)
                result.append(subres)


        return result

        
        