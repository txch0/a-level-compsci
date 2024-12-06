import re
data = open("aoc-d3-input.txt", "r")
alltext = data.read()

pattern = "mul\((\d{1,3}),\s*(\d{1,3})\)"

matches = re.findall(pattern, alltext)

total = 0
for match in matches:
    val = match[0]
    mult = match[1]

    print(val, mult)
    total += (int(val) * int(mult))

print(total)