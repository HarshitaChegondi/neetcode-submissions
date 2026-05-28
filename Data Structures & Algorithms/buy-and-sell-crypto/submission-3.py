class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        minProfit = float('inf')

        for p in prices:
            if p<minProfit:
                minProfit = p
            best = max(best, p-minProfit)
        
        return best
            

        




        