import pytest


def binary_search(nums: list[int], target: int):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


@pytest.mark.parametrize(
    "nums,target,expected",
    [([*range(5)], 2, 2), ([*range(5)], 6, -1), ([*range(20, 50)], 21, 1)],
)
def test_binary_search(nums: list[int], target: int, expected: int):
    assert binary_search(nums, target) == expected
