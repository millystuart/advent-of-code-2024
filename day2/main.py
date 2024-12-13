file = open("/home/milly/Code/python/advent-of-code-2024/day2/input.txt", "r")
safe_tally = 0

# function to check if gaps between levels are between 1 and 3 inclusive
def check_safe_levels(line):
    for i in range (0, len(line) - 1):
        if (abs(line[i] - line[i + 1]) < 1 or abs(line [i] - line[i + 1]) > 3):
            return False
    return True
    
# get each line in file and check differences
for line in file:
    split_line = line.split(" ")

    # cast all strings in list as ints
    line = list(map(int, split_line))

    # check if line is increasing
    if (line == sorted(line)):
        if (check_safe_levels(line) == True):
            safe_tally += 1
    elif (line == sorted(line, reverse = True)):
        if (check_safe_levels(line) == True):
            safe_tally += 1

file.close()

print(safe_tally)

# ------------------------------ Part 2 ------------------------------ #
