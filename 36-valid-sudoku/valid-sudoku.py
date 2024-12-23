class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subGrid = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if (number == "."):
                    continue
                if number in rows[i]:
                    return False
                rows[i].add(number)
                if number in cols[j]:
                    return False
                cols[j].add(number)
                index_grid = (i // 3) * 3 + (j // 3)
                if number in subGrid[index_grid]:
                    return False
                subGrid[index_grid].add(number)
        return True
        