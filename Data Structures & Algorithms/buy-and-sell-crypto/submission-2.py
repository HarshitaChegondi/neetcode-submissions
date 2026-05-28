class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_num = prices[0]
        max_diff = float('-inf')

        for i in range(1, len(prices)):
            diff = prices[i] - min_num
            max_diff = max(max_diff, diff)
            min_num = min(min_num, prices[i])  

        if max_diff > 0:
            return max_diff
        else:
            return 0
        

        