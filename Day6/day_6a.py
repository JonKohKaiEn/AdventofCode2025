with open("./day_6_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# with open("./day_6_test.txt", "r") as f:
#     input_txt = [s.rstrip("\n") for s in f.readlines()]

from functools import reduce

input_txt = [line.split() for line in input_txt]

problems = []
for col in range(len(input_txt[0])):
    problem = [row[col] for row in input_txt]
    problems.append(problem)

total = 0
for problem in problems:
    if problem[-1] == "*":
        total += reduce(lambda a, b: a * b, [int(e) for e in problem[:-1]])
    else:
        total += sum([int(e) for e in problem[:-1]])

print(total)
