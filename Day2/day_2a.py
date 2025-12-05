with open("day_2_input.txt", "r") as f:
    input_txt = f.readline().split(",")

total = 0
for id_range in input_txt:
    start_id, end_id = id_range.split("-")
    for id in range(int(start_id), int(end_id) + 1):
        id_str = str(id)
        if len(id_str) % 2 != 0:
            continue
        id_midpt = int(len(id_str) / 2)
        if id_str[:id_midpt] == id_str[id_midpt:]:
            total += id

print(total)
