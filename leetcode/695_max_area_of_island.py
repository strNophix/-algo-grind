class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        biggest_island = 0
        counter = 0

        def dfs(row: int, col: int):
            nonlocal counter
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return

            if grid[row][col] != 1:
                return

            counter += 1
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    biggest_island = max(biggest_island, counter)
                    counter = 0

        return biggest_island
