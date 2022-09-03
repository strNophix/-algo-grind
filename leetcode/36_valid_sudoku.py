from typing import List
import pytest


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, cubes = set(), set(), set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if not val.isdigit():
                    continue

                cube = (i // 3) * 3 + (j // 3)
                if (i, val) in rows or (j, val) in cols or (cube, val) in cubes:
                    return False

                rows.add((i, val))
                cols.add((j, val))
                cubes.add((cube, val))

        return True


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "sudoku, expected",
    [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        )
    ],
)
def test_search(solution: Solution, sudoku: List[List[str]], expected: bool):
    assert solution.isValidSudoku(sudoku) == expected
