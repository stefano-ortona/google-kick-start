def check_sudoku(grid, n):
    return len(grid) == n*n and len(grid[0]) == n*n and \
           check_rows(grid, n) and check_columns(grid, n) and check_sub_squares(grid, n)


def check_rows(grid, n):
    for i in range(n*n):
        seen = [False for k in range(n*n + 1)]
        for j in range(n*n):
            if grid[i][j] <= 0 or grid[i][j] > n*n or seen[grid[i][j]]:
                return False
            seen[grid[i][j]] = True
    return True


def check_columns(grid, n):
    for j in range(n*n):
        seen = [False for k in range(n*n + 1)]
        for i in range(n*n):
            if seen[grid[i][j]]:
                return False
            seen[grid[i][j]] = True
    return True


def check_sub_squares(grid, n):
    row, col = 0, 0
    while row < len(grid):
        if not check_one_square(grid, row, col, n):
            return False
        col += n
        if col >= len(grid[0]):
            row += n
            col = 0
    return True


def check_one_square(grid, i, j, n):
    seen = [False for k in range(n * n + 1)]
    for row in range(i, i+n):
        for col in range(j, j+n):
            if seen[grid[row][col]]:
                return False
            seen[grid[row][col]] = True
    return True


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        grid = []
        for j in range(n*n):
            grid.append([int(s) for s in input().split(' ')])
        sol = "Yes" if check_sudoku(grid, n) else "No"
        print("Case #{}: {}".format(i, sol))

