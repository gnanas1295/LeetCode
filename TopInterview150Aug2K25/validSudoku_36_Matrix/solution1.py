from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        if not board:
            return False
        # row checks
        for i in range(len(board)):
            seenInRow = set()
            for j in range(9):
                number = board[i][j]
                if number == ".":
                    continue
                if number in seenInRow:
                    return False
                seenInRow.add(number)
        print("Valid Row")

        for j in range(9):
            seenInCol = set()
            for i in range(9):
                number = board[i][j]

                if number == ".":
                    continue
                if number in seenInCol:
                    return False

                seenInCol.add(number)

        # Valid Columns

        for boxRow in range(3):
            for boxCol in range(3):

                seenInBox = set()

                for i in range(3):
                    for j in range(3):
                        rowValue = boxRow * 3 + i
                        colValue = boxCol * 3 + j
                        number = board[rowValue][colValue]

                        if number == ".":
                            continue

                        if number in seenInBox:
                            return False
                        seenInBox.add(number)
        return True
