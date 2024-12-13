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

    # check if line is increasing/decreasing
    if (line == sorted(line) or line == sorted(line, reverse = True)):
        if (check_safe_levels(line) == True):
            safe_tally += 1

file.close()

print(safe_tally)

# ------------------------------ Part 2 ------------------------------ #

file = open("/home/milly/Code/python/advent-of-code-2024/day2/input.txt", "r")
safe_tally2 = 0

# function to check if a line is valid with problem dampener
def problem_dampener_check(line):
    # usual check from part 1
    if (line == sorted(line) or line == sorted(line, reverse = True)):
        if check_safe_levels(line):
            return True

    # Check if removing a single number makes the line valid
    for i in range(0, len(line)):
        modified_line = []
        for j in range (0, len(line)):
            if j != i:
                modified_line.append(line[j])
        
        if modified_line == sorted(modified_line) or modified_line == sorted(modified_line, reverse=True):
            if check_safe_levels(modified_line):
                return True

    return False

for line in file:
    split_line = line.split()

    # cast all strings in list as ints
    line = list(map(int, split_line))

    # check if the line is valid
    if problem_dampener_check(line) == True:
        safe_tally2 += 1

file.close()

print(safe_tally2) 