class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        max_ones = 0
        max_row_idx = 0
        
        for i, row in enumerate(mat): # iterate over all rows
            num_ones = 0
            for n in row: # iterate over elements in a row
                if n == 1: # count number of ones in a row
                    num_ones += 1
                
                if num_ones > max_ones:
                    max_ones = num_ones
                    max_row_idx = i
                    
        return [max_row_idx, max_ones]
            
        