class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in range(len(matrix)):
            l_pos = len(matrix[r]) - 1
            if matrix[r][l_pos] < target:
                continue
            else:
                l = 0
                right = len(matrix[r]) - 1

                while l <= right:
                    middle = (l + right) // 2
                
                    if matrix[r][middle] == target:
                        return True
                    elif matrix[r][middle] < target:
                        l = middle + 1
                    else:
                        right = middle - 1
                return False


        return False               


        
        