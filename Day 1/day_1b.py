# with open('day_1_input.txt', 'r') as f:
#     input_txt = [s.rstrip('\n') for s in f.readlines()]
input_txt = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

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
                count += 1
            else:
                dial += amount
                if dial == 0:
                    count += 1
                break
        else:
            if dial - amount < 0:
                amount -= dial + 1
                dial = 99
                count += 1
            else:
                dial -= amount
                if dial == 0:
                    count += 1
                break

        print(dial, amount)

print(count)