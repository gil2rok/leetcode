class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        sorted_grid = [[None] for i in range(len(grid))]
        for row in grid:
            row.sort(reverse=True)
            
        res = 0
        for i in range(len(grid[0])):
            col_max = grid[0][i]
            for row in grid:
                col_max = max(col_max, row[i])
            res += col_max
        return res
        