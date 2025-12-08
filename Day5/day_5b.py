with open("./day_5_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# with open("./day_5_test.txt", "r") as f:
#     input_txt = [s.rstrip("\n") for s in f.readlines()]

fresh_ranges = list()
for line in input_txt:
    if "-" in line:
        n1, n2 = line.split("-")
        fresh_ranges.append([int(n1), int(n2)])

print(fresh_ranges)

# merged_ranges = [fresh_ranges[0]]
# for curr_1, curr_2 in fresh_ranges[1:]:
#     print(f"Checking {(curr_1, curr_2)}")
#     idx_1, idx_2 = -1, -1
#     for i in range(len(merged_ranges)):
#         if merged_ranges[i][0] <= curr_1 <= merged_ranges[i][1]:
#             idx_1 = i
#         if merged_ranges[i][0] <= curr_2 <= merged_ranges[i][1]:
#             idx_2 = i
#     print(f"idx_1: {idx_1} \t idx_2: {idx_2}")
#
#     if idx_1 != -1:
#         if idx_2 != -1:
#             print(f"Merging with {idx_1} and {idx_2}")
#             # if both ends can be merged
#             temp_list = [
#                 merged_ranges[i]
#                 for i in range(len(merged_ranges))
#                 if i not in [idx_1, idx_2]
#             ]
#             temp_list.append([merged_ranges[idx_1][0], merged_ranges[idx_2][1]])
#             merged_ranges = temp_list
#         else:
#             # if left end can be merged
#             merged_ranges[idx_1][1] = curr_2
#             print(f"Merging with {idx_1}")
#     elif idx_2 != -1:
#         # if right end can be merged
#         merged_ranges[idx_2][0] = curr_1
#         print(f"Merging with {idx_2}")
#     else:
#         # no merge
#         merged_ranges.append([curr_1, curr_2])
#         print("Appending")
#
#     print(merged_ranges)
#     print(len(merged_ranges))

fresh_ranges.sort(key=lambda x: x[0])
merged_ranges = []
for curr_start, curr_end in fresh_ranges:
    if not merged_ranges:
        merged_ranges.append([curr_start, curr_end])
    else:
        last_start, last_end = merged_ranges[-1]
        if curr_start <= last_end + 1:
            merged_ranges[-1][1] = max(last_end, curr_end)
        else:
            merged_ranges.append([curr_start, curr_end])

count = 0
for r in merged_ranges:
    count += r[1] - r[0] + 1
print(count)
