with open('day_1_input.txt', 'r') as f:
    input_txt = [s.rstrip('\n') for s in f.readlines()]

count = 0
dial = 50
for rotation in input_txt:
    direction = rotation[0]
    amount = int(rotation[1:])
    while True:
        if direction == 'R':
            if dial + amount > 99:
                amount -= 100 - dial
                dial = 0
            else:
                dial += amount
                if dial == 0:
                    count += 1
                break
        else:
            if dial - amount < 0:
                amount -= dial + 1
                dial = 99
            else:
                dial -= amount
                if dial == 0:
                    count += 1
                break

print(count)