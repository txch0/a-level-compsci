text = open("aoc-d2-input.txt")

safecount = 0

for line in text:
    vals = line.strip().split(" ")

    # Convert all values to integers
    vals = list(map(int, vals))
    
    diffs = []
    
    # Calculate differences between adjacent values
    for i in range(1, len(vals)):
        diffs.append(vals[i] - vals[i-1])

    # Check if differences meet the criteria
    is_increasing = all(d > 0 for d in diffs)  # All differences should be positive (increasing)
    is_decreasing = all(d < 0 for d in diffs)  # All differences should be negative (decreasing)
    valid_diffs = all(1 <= abs(d) <= 3 for d in diffs)  # All diffs should be between 1 and 3

    if (is_increasing or is_decreasing) and valid_diffs:
        safecount += 1
        print("Safe:", vals, diffs)
    else:
        print("Unsafe:", vals, diffs)

print("Safe reports count:", safecount)