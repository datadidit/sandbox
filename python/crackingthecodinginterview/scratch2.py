import copy

def all_uptodate(rows, columns, grid):
    for row_idx in range(rows):
        for column_idx in range(columns):
            current = grid[row_idx][column_idx]
            if current != 1:
                return False
    return True


def update_grid(rows, columns, grid):
    new_grid = copy.deepcopy(grid)
    for row_idx in range(rows):
        for column_idx in range(columns):
            current = grid[row_idx][column_idx]
            left = grid[row_idx][column_idx - 1] if column_idx - 1 > 0 else None
            right = grid[row_idx][column_idx + 1] if column_idx + 1 < columns else None
            bottom = grid[row_idx + 1][column_idx] if row_idx + 1 < rows else None
            above = grid[row_idx - 1][column_idx] if row_idx - 1 > 0 else None

            # Update left
            if current == 1 and left is not None and left == 0:
                new_grid[row_idx][column_idx - 1] = 1
            # Update right
            if current == 1 and right is not None and right == 0:
                new_grid[row_idx][column_idx + 1] = 1

            # Update bottom
            if current == 1 and bottom is not None and bottom == 0:
                new_grid[row_idx + 1][column_idx] = 1

            # Update Top
            if current == 1 and above is not None and above == 0:
                new_grid[row_idx - 1][column_idx] = 1

    return new_grid


def minimumDays(rows, columns, grid):
    # WRITE YOUR CODE HERE
    for i in range(rows * columns): # Max days
        # Print Grid
        print("Day %s" % i)
        for i in range(len(grid)):
            print(grid[i])
        updated_grid = update_grid(rows, columns, grid)
        if all_uptodate(rows, columns, updated_grid):
            return i
        grid = copy.deepcopy(updated_grid)

    return rows * columns


if __name__ == "__main__":
    t1 = [[1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]
    print(minimumDays(5, 5, t1))