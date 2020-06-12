total = 0

with open('numbers.txt', 'r') as inp, open('output.txt', 'w') as outp:
    for line in inp:
        num = float(line)
        outp.write(str(num*num))
        outp.write("\n")
