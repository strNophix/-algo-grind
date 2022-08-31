import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            breakpoint()
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # ([2, 5, 6, 0, 0, 1, 2], 0, True),
        # ([2, 5, 6, 0, 0, 1, 2], 3, False),
        ([1, 0, 1, 1, 1], 0, True),
    ],
)
def test_search(solution: Solution, nums: list[int], target: int, expected: bool):
    assert solution.search(nums, target) == expected
