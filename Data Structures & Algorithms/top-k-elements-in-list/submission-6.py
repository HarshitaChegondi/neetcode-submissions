class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1 
            else:
                dict[n] = 1

        topVal = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:k]


        return [item[0] for item in topVal]
        