class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[None] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                tl = self.find_tl(i, j, grid)
                br = self.find_br(i, j, grid)
                ans[i][j] = abs(tl - br)
        return ans
                
    def find_tl(self, r, c, grid):
        top_left = set()

        r_new, c_new = r-1, c-1
        while r_new >=0 and c_new >= 0:
            val = grid[r_new][c_new]
            top_left.add(val)
            
            r_new -= 1 
            c_new -= 1

        return len(top_left)
        
    def find_br(self, r, c, grid):
        m, n = len(grid), len(grid[0])
        bottom_right = set()

        r_new, c_new = r+1, c+1 
        while r_new < m and c_new < n:
            val = grid[r_new][c_new]
            bottom_right.add(val)
            
            r_new += 1
            c_new += 1
        
        return len(bottom_right)

        