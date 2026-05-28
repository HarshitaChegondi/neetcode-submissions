class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        flag = 0
        counter = 0

        for i in range(len(temperatures)):
            temp = i+1
            while temp < len(temperatures) and temperatures[temp] <= temperatures[i]:
                temp += 1
            stack.append(temp-i if temp< len(temperatures) else 0)

        return stack
        

                           


                

