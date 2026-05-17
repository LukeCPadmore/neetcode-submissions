class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        COLS,ROWS = len(matrix[0]),len(matrix)
        l = 0 
        r = ROWS - 1
        # Filter to row
        while l <=r:
            m = (l+r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                break
            elif target <= matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        # Perform regular binary search
        rowFound = m
        l,r = 0, COLS - 1
        while l <=r:
            m = (l+r) // 2
            if matrix[rowFound][m] == target:
                return True
            elif target < matrix[rowFound][m]:
                r = m - 1
            else:
                l = m + 1
        return False
