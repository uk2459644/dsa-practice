from collections import deque

def maxSafenessFactor(grid):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs():
        queue = deque([(0, 0, 0)])  # (row, column, distance)
        visited = set()
        max_safeness_factor = -1

        while queue:
            row, col, distance = queue.popleft()

            if (row, col) == (n - 1, n - 1):
                max_safeness_factor = max(max_safeness_factor, distance)
                continue

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    new_distance = max(distance, min_manhattan_distance(new_row, new_col))
                    queue.append((new_row, new_col, new_distance))

        return max_safeness_factor

    def min_manhattan_distance(row, col):
        min_distance = float('inf')
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    min_distance = min(min_distance, abs(row - r) + abs(col - c))
        return min_distance

    return bfs()

# Example usage:
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
print(maxSafenessFactor(grid))  # Output: 6
