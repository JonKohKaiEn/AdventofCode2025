with open('day_1_input.txt', 'r') as f:
    input_txt = [s.rstrip('\n') for s in f.readlines()]
# input_txt = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
# input_txt = ['L55']

count = 0
dial = 50
for rotation in input_txt:
    print(rotation)
    direction = rotation[0]
    amount = int(rotation[1:])
    if direction == 'R':
        crossing, remainder = divmod(dial+amount, 100)
        count += crossing
        dial = remainder
    else:
        crossing, remainder = divmod(dial-amount, 100)
        if dial == 0:
            count += abs(crossing) - 1
        else:
            count += abs(crossing)
        dial = remainder
        if dial == 0:
            count += 1

    print(dial, count)

print(count)