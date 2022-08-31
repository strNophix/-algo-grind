import pytest
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("", [])
def test_search(solution: Solution):
    pass
