"""
Search a 2D Matrix
Medium

You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        matrix is sorted in non-decreasing order -> you can take binary_search
        if you gonna use binary search, you have to treat matrix as a normal 1-D interger array
        """
        # m ... the length of rows
        # n ... the length of columns
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1

        while l <= r:
            mid = l + ((r - l)//2)
            
            if target == matrix[mid//n][mid%n]:
                return True
            elif target < matrix[mid//n][mid%n]:
                r = mid - 1
            else:
                l = mid + 1
        return False