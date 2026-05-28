class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in numbers:
                j = numbers.index(num, i + 1)
                res.append(i + 1)
                res.append(j + 1)
                break

        return(res)