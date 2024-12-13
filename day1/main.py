left_list = []
right_list = []
distances = []

file = open("/home/milly/Code/python/advent-of-code-2024/day1/input.txt", "r")

# split file into two separate lists for comparison
for line in file:
    split_line = line.split("   ")
    left = int(split_line[0])
    right = int(split_line[1])
    left_list.append(left)
    right_list.append(right)

file.close()

# sort the lists in ascending order
left_list.sort()
right_list.sort()

# gather distances between two lists
for i in range(0, len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    distances.append(distance)

# sum distances
print(sum(distances))

# ------------------------------ Part 2 ------------------------------ #

similarity_score = []

# calculate number of occurences of left_list in right_list
for lnum in left_list:
    occurence = 0
    for rnum in right_list:
        if lnum == rnum:
            occurence += 1
    similarity_value = lnum * occurence
    similarity_score.append(similarity_value)

# sum occurences

print(sum(similarity_score))