import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # The first item of first ascending sequence is always bigger than the first item of the second ascending sequence.
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid

            # If the current item is bigger than the first item of the first ascending sequence we know that nums[low:mid] is sorted.
            # Otherwise we know that the current mid is on the edge of the second ascending sequence.
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

        return -1


@pytest.fixture
def solution():
    return Solution()


def test_search(solution: Solution):
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
