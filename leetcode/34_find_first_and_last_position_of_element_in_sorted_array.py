import typing
import pytest

FindFn = typing.Callable[[int], bool]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.binary_search(nums, target, lambda v: v >= target)
        end = self.binary_search(nums, target, lambda v: v > target)
        return [start, end]

    def binary_search(self, nums: list[int], target: int, fn: FindFn) -> int:
        res = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                res = mid

            if fn(nums[mid]):
                high = mid - 1
            else:
                low = mid + 1

        return res


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 2, [0, 1]),
    ],
)
def test_search_range(
    solution: Solution, nums: list[int], target: int, expected: list[int]
):
    assert solution.searchRange(nums, target) == expected
