class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        seen = {}
 

        for i, val in enumerate(numbers, start = 1):
            complement = target - val
            if complement in seen :
                res.append(seen[complement])
                res.append(i)
            seen[val] = i

        return res
