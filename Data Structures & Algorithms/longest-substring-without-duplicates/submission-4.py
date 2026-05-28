class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bestLen = 0
        res = []
        for i in s:
            if i in res:
                delIndex = res.index(i)
                res= res[delIndex+1:]
                res.append(i)
            if i not in res:
                res.append(i)
                currentArraylength = len(res)
                bestLen = max(bestLen, currentArraylength)

        return bestLen