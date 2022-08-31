import pytest


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2

            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "matrix, target, expected",
    [([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)],
)
def test_search(
    solution: Solution, matrix: list[list[int]], target: int, expected: bool
):
    assert solution.searchMatrix(matrix, target) == expected
