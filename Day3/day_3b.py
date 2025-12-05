with open("./day_3_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# input_txt = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

total = 0
k = 12
for bank in input_txt:
    stack = []
    attempts = len(bank) - k
    for battery in bank:
        while attempts > 0 and stack and int(stack[-1]) < int(battery):
            stack.pop()
            attempts -= 1
        stack.append(battery)
    total += int("".join(stack[:k]))

print(total)
