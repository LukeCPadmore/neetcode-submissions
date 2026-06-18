class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr: List[int ]) -> bool: 
            l,r = 0, len(arr) - 1 
            while l<=r:
                m = l + (r-l) // 2
                if arr[m] == target:
                    return True 
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        up, low = 0, len(matrix) - 1 
        while up < low:
            m = (up + low) // 2
            print(f'up={up}, low={low}, m={m}')
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                print(matrix[m])
                return binary_search(matrix[m])
            elif matrix[m][-1] < target:
                up = m + 1
            else:
                low = m - 1
        print(f'up={up}, low={low}')
        return binary_search(matrix[low])
