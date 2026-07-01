class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1

        which_row = -1

        while i <= j:
            mid = (j-i)//2 + i

            start = matrix[mid][0]
            end = matrix[mid][-1]

            if start <= target <= end:
                which_row = mid
                break
            
            if target < start:
                j = mid - 1
            else:
                i = mid + 1

        if which_row == -1: 
            return False

        k = 0
        l = len(matrix[0]) - 1
        arr = matrix[which_row]

        while k <= l:
            mid = ((l - k) // 2)  + k

            if arr[mid] == target:
                return True
            
            if arr[mid] > target:
                l = mid - 1
            else:
                k = mid + 1
        
        return False


