class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        arr = set()
        flag = 0
        for i in nums:
            if i not in arr:
                arr.add(i)
            else:
                flag = flag+1

        if flag != 0:
            return True
        else:
            return False