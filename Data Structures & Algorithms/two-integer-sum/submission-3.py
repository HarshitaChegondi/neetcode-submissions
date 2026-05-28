class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []

        for i in range(len(nums)):
            difference=0
            difference = target - nums[i]
            if difference in nums:
                arr = [i, nums.index(difference)]
        return sorted(arr)