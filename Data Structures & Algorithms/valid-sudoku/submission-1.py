class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ''' 
        use defaultdicts so we don't have to worry about missing keys
        nor do we have to worry about initializing it as a set
        '''
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # we know how many rows and columns there will be in the set
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
                