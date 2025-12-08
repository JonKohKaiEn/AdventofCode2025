with open("./day_5_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# with open("./day_5_test.txt", "r") as f:
#     input_txt = [s.rstrip("\n") for s in f.readlines()]

fresh_ranges, ids = list(), list()
for line in input_txt:
    if line:
        if "-" in line:
            n1, n2 = line.split("-")
            fresh_ranges.append((int(n1), int(n2)))
        else:
            ids.append(int(line))

fresh_set = set()
for fresh_range in fresh_ranges:
    fresh_set.update(set(id for id in ids if fresh_range[0] <= id <= fresh_range[1]))

print(len(fresh_set))
