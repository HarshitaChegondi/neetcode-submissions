class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lenofUnique = len(set(nums))

        if((len(nums)) != lenofUnique):
             return True
        else:
            return False  