class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                cur_sum = self.hourglass_sum(grid, i, j)
                max_sum = max(max_sum, cur_sum)
                
        return max_sum
               
    def hourglass_sum(self, grid, i,j):
        top = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
        mid = grid[i][j]
        bottom = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
        return top + mid + bottom
        