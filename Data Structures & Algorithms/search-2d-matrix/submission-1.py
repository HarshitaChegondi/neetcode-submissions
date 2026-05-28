class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    count = count+1
    
        if count >= 1:
            return True
        else:
            return False
        