from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the indices of numbers
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate the required number to form the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store the current number's index
            num_to_index[num] = i
