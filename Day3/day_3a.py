with open("./day_3_input.txt", "r") as f:
    input_txt = f.readlines()
# input_txt = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

total = 0
for bank in input_txt:
    largest_n = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            test_n = int(bank[i] + bank[j])
            if test_n > largest_n:
                largest_n = test_n
    total += largest_n

print(total)
