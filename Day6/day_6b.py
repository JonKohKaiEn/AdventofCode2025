with open("./day_6_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# with open("./day_6_test.txt", "r") as f:
#     input_txt = [s.rstrip("\n") for s in f.readlines()]

from functools import reduce

input_transpose = []
for i in range(len(input_txt[0])):
    input_transpose.append("".join(line[i] for line in input_txt))
input_transpose.reverse()
# print(input_transpose)

gap_ref = " " * len(input_txt)
total = 0

while input_transpose:
    if gap_ref in input_transpose:
        for i, s in enumerate(input_transpose):
            if s == gap_ref:
                break_idx = i
                break

    problem = input_transpose[:break_idx]
    problem = [s.replace(" ", "") for s in problem]
    # print(problem)

    numbers = []
    operator = ""
    for ele in problem:
        if "*" in ele:
            numbers.append(int(ele[:-1]))
            operator = "*"
        elif "+" in ele:
            numbers.append(int(ele[:-1]))
            operator = "+"
        else:
            numbers.append(int(ele))

    if operator == "*":
        total += reduce(lambda a, b: a * b, numbers)
    else:
        total += sum(numbers)

    if gap_ref in input_transpose:
        input_transpose = input_transpose[break_idx + 1 :]
    else:
        break

print(total)
