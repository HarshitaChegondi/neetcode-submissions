class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        prod = 1
        
        
        for i in range(len(nums)):
            otherElements = nums[:i]+nums[i+1:]
            print(otherElements)
            for x in otherElements:
                prod = prod*x
            result.append(prod)
            prod = 1

        return result



                    
            

            
