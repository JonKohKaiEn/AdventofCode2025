with open("./day_4_input.txt", "r") as f:
    input_txt = [s.rstrip("\n") for s in f.readlines()]
# with open("./day_4_test.txt", "r") as f:
#     input_txt = [s.rstrip("\n") for s in f.readlines()]


grid = [[c for c in row] for row in input_txt]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            rolls = 0
            for d in directions:
                if (
                    (0 <= i + d[0] < len(grid))
                    and (0 <= j + d[1] < len(grid[0]))
                    and (grid[i + d[0]][j + d[1]] == "@")
                ):
                    rolls += 1
            if rolls < 4:
                count += 1

print(count)
