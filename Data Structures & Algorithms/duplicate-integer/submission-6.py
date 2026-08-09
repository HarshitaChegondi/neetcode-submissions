class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        arr = set()
        for n in nums:
            if n not in arr:
                arr.add(n);
            else:
                return True
        return False