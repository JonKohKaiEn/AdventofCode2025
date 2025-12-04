with open("day_2_input.txt", "r") as f:
    input_txt = f.readline().split(",")
# input_txt = [
#     "11-22",
#     "95-115",
#     "998-1012",
#     "1188511880-1188511890",
#     "222220-222224",
#     "1698522-1698528",
#     "446443-446449",
#     "38593856-38593862",
#     "565653-565659",
#     "824824821-824824827",
#     "2121212118-2121212124",
# ]

total = 0
for id_range in input_txt:
    start_id, end_id = id_range.split("-")
    count = 0
    for id in range(int(start_id), int(end_id) + 1):
        id_str = str(id)
        id_len = len(id_str)
        for i in range(1, int(id_len / 2) + 1):
            if id_len % i != 0:
                continue
            if id_str[:i] * int(id_len / i) == id_str:
                total += id
                break

print(total)
