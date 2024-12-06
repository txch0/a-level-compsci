def count_word_occurrences(grid, word):
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check all rows (left to right and right to left)
    for row in grid:
        count += row.count(word)  # Check "XMAS"
        count += row.count(word[::-1])  # Check "SAMX"
    
    # Check all columns (top to bottom and bottom to top)
    for col in range(cols):
        column_str = ''.join([grid[row][col] for row in range(rows)])
        count += column_str.count(word)  # Check "XMAS"
        count += column_str.count(word[::-1])  # Check "SAMX"
    
    # Check diagonals (top-left to bottom-right and bottom-left to top-right)
    for r in range(rows):
        for c in range(cols):
            # Top-left to bottom-right diagonal
            if r + word_len <= rows and c + word_len <= cols:
                diagonal_str = ''.join(grid[r + i][c + i] for i in range(word_len))
                count += (diagonal_str == word) or (diagonal_str == word[::-1])
            
            # Bottom-left to top-right diagonal
            if r - word_len + 1 >= 0 and c + word_len <= cols:
                diagonal_str = ''.join(grid[r - i][c + i] for i in range(word_len))
                count += (diagonal_str == word) or (diagonal_str == word[::-1])

    return count

# Read input file
with open("aoc-d4-input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

# The word to find
word = "XMAS"

# Find occurrences
count = count_word_occurrences(grid, word)
print(count)
