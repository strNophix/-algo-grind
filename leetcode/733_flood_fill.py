import pytest


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        orig = image[sr][sc]

        def dfs(i: int, j: int):
            if (
                0 <= i < len(image)
                and 0 <= j < len(image[0])
                and image[i][j] == orig
                and image[i][j] != color
            ):
                image[i][j] = color
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        dfs(sr, sc)
        return image


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "image, sr, sc, color, expected",
    [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]])],
)
def test_search(
    solution: Solution,
    image: list[list[int]],
    sr: int,
    sc: int,
    color: int,
    expected: list[list[int]],
):
    assert solution.floodFill(image, sr, sc, color) == expected
