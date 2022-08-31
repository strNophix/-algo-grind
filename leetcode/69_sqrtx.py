import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            val = mid * mid
            if val <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < val:
                right = mid - 1
            else:
                left = mid + 1
        return 0


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("x, expected", [(4, 2), (8, 2)])
def test_my_sqrt(solution: Solution, x: int, expected: int):
    assert solution.mySqrt(x) == expected
