class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}
        res = []
        for n in nums:
            if n not in myDict:
                myDict[n] = 1
            else:
                myDict[n] += 1
        
        res = sorted(myDict, key= myDict.get, reverse=True)[:k]
        return res
        
            


            


