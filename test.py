def solve_n_queens(n):
    def is_valid(board, row, col):
        for r, c in board:
            if col == c or row + col == r + c or row - col == r - c:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                backtrack(board, row + 1)
                board.pop()
                
    result = []
    backtrack([], 0)
    return [[col for row, col in solution] for solution in result]

print(solve_n_queens(5))