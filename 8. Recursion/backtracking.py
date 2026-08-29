"""
Backtracking is:
Try → Explore → Undo → Try something else
You build a solution step by step, and when a path doesn't work, you go back and change choices.
"""

"""
The Core Idea (Very Important)
At every step, you:
  Choose an option
  Explore further (recursive call)
  Un-choose (backtrack)
"""

# Generic Backtracking Template (MEMORIZE)
def backtrack(path, options):
    if base_case:
        result.append(path[:])
        return

    for choice in options:
        # choose
        path.append(choice)

        # explore
        backtrack(path, new_options)

        # un-choose
        path.pop()


# Example: N-Queens Problem
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    result = []

    def backtrack_inner(row):
        if row == n:
            result.append([row[:] for row in board])
            return

    backtrack_inner(0)


solve_n_queens(4)
# print(result)
