class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictionary = {}
        for key in nums:
            if key not in dictionary:
                dictionary[key] = 1
            else:
                return True
        return False


        
        