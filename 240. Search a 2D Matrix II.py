class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            if target in matrix[i]:
                return 1
        return 0
        