class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        dictionary = {}
        for n in nums:
            if n not in dictionary:
                    dictionary[n] = 1
            else:
                dictionary[n] += 1

        sortedValues = dict(sorted(dictionary.items(), key=lambda item:item[1], reverse=True)[:k])
        return list(sortedValues.keys())

        