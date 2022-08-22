# Valid Sudoku

"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1- Each row must contain the digits 1-9 without repetition.
We can use HashSet to for every row to check if shouldn't contain any duplicate.
2- Each column must contain the digits 1-9 without repetition.
We can use HashSet to for every column to check if shouldn't contain any duplicate.

Tricky:
3- Each of the 9 cells for '3x3 sub-boxes' of the grid must contain the digits 1-9 without repetition.
We can use HashSet to for every 3x3 sub-box to check if shouldn't contain any duplicate.
4- A partially filled sudoku which is valid. 
We don't consider the filled cells in this problem. A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
For example, the following sudoku is partially filled:

j j j j j j j j 
1 2 3 4 5 6 7 8 .
                1 i
                2 i
                3 i
                4 i
                5 i
                6 i
                7 i
                8 i
                9 i

'.' is the empty cell in the sudoku above that can be filled with any 1 or 9 digit. Since, we don't need to fill the empty cells, we can just show sudoku is valid.

- Adding and checking for duplicate in each row and column from hash set is O(1) time complexity which makes the overall time complexity O(9^2) time and space complexity O(9^2) space where 9 is the size of the sudoku because we are evaluating every element in the sudoku.

- Duplicate can be found with hashSet but you can use array as well.
"""

from typing import List
import collections

# O(9^2) time and O(9^2) space coz we are evaluating every element in the sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set)  # grid's key = (r /3, c /3) | 3x3 sub-boxes

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if the cell is empty, we don't need to check for duplicate
                    continue
                # if we have duplicate in any of the row, column, or grid, return False
                if ( 
                    board[r][c] in rows[r] # for every cell in row
                    or board[r][c] in cols[c] # for every cell in column
                    or board[r][c] in grid[(r // 3, c // 3)] # for every cell in grid
                ):
                    return False
                # finally, add the cell to the set of row, column, and grid
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])

        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        # i is the index of the row
        # j is the index of the column
        # c is the column's value
        # row is the complete row
        seen = []
        for i, row in enumerate(board):
            # print(i, row), i is index of row
            # 0 ['5', '3', '.', '.', '7', '.', '.', '.', '.']
            # 1 ['6', '.', '.', '1', '9', '5', '.', '.', '.']
            # 2 ['.', '9', '8', '.', '.', '.', '.', '6', '.']
            # 3 ['8', '.', '.', '.', '6', '.', '.', '.', '3']
            # 4 ['4', '.', '.', '8', '.', '3', '.', '.', '1']
            # 5 ['7', '.', '.', '.', '2', '.', '.', '.', '6']
            # 6 ['.', '6', '.', '.', '.', '.', '2', '8', '.']
            # 7 ['.', '.', '.', '4', '1', '9', '.', '.', '5']
            # 8 ['.', '.', '.', '.', '8', '.', '.', '7', '9']
            for j, c in enumerate(row):
                # print(j, c) # j is index of column
                # 0 ['5', '3', '.', '.', '7', '.', '.', '.', '.']
                # 0 5
                # 1 3
                # 2 .
                # 3 .
                # 4 7
                # 5 .
                # 6 .
                # 7 .
                # 8 .
                #print(i, c)
                # 0 5
                # 0 3
                # 0 .
                # 0 .
                # 0 7
                # 0 .
                # 0 .
                # 0 .
                # 0 .
                # 1 6
                # print(j, c)
                # 0 5
                # 1 3
                # 2 .
                # 3 .
                # 4 7
                # 5 .
                # 6 .
                # 7 .
                # 8 .
                # 0 6
                # print(i/3, j/3, c)
                # 0 0 5
                # 0 0 3
                # 0 0 .
                # 0 1 .
                # 0 1 7
                # 0 1 .
                # 0 2 .
                # 0 2 .
                # 0 2 .
                # 0 0 6
                if c != '.':
                    seen += ((i, c), (c, j), (i/3, j/3, c))
                    # print(len(seen))
        return len(seen) == len(set(seen)) 
    
    # or one line solution
    def isValidSudoku3(self, board: List[List[str]]) -> bool:
        # i is the index of the row
        # j is the index of the column
        # c is the column's value
        # row is the complete row
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# print(Solution().isValidSudoku(board)) # True
print(Solution().isValidSudoku2(board)) # True
# print(Solution().isValidSudoku3(board)) # True