from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.neetcode_sol(board)
        
        #return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)
    
    def neetcode_sol(self, board):
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        square_dict = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                    
                if (board[r][c] in row_dict[r] or
                    board[r][c] in col_dict[c] or
                    board[r][c] in square_dict[(r//3, c//3)]):
                        return False
                    
                row_dict[r].add(board[r][c])
                col_dict[c].add(board[r][c])
                square_dict[(r//3, c//3)].add(board[r][c])
        return True
                
        
        
    def isValidRow(self, board):
        
        # loop over rows
        for row in board:
            # count how many times visited a number 1-9
            visited = [0] * 9
            
            # extract filled in nums in O(1)
            nums = [int(e) for e in row if e != '.']

            # use n-1 for 0-based indexing
            for n in nums:
                if visited[n - 1] == 1:
                    return False
                else:
                    visited[n - 1] += 1
                    
        return True

    def isValidCol(self, board):
        # loop over cols
        for c in range(9):
            # count how many times visited a number 1-9
            visited = [0] * 9
            
            # extract filled in nums in O(1)
            nums = [int(board[r][c]) for r in range(9) if board[r][c] != '.']
            
            # use n-1 for 0-based indexing
            for n in nums:
                if visited[n - 1] == 1:
                    return False
                else:
                    visited[n - 1] += 1
                    
        return True
    
    def isValidSquare(self, board):
        rstart_list = [0,3,6]
        cstart_list = [0,3,6]
        
        for rstart in rstart_list:
            for cstart in cstart_list:
                # init nums array
                nums = []
                
                # loop over 3x3 square
                for r in range(rstart, rstart+3):
                    for c in range(cstart, cstart+3):
                        
                        # append valid nums to list
                        if board[r][c] != '.':
                            nums.append(int(board[r][c]))    

                # count how many times visited a number 1-9
                visited = [0]*9
                for n in nums:
                    if visited[n - 1] == 1:
                        return False
                    else:
                        visited[n - 1] += 1
                                        
        return True