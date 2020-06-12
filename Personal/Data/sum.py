total = 0

with open('numbers2.txt', 'r') as inp:
    for line in inp:
        num = float(line)
        total += num

print('Total of all numbers: {}'.format(total))
