# open file with company names and positions
inF = open("/Users/billli/Projects/Python/scripts/clas/unsorted.txt", "r")
outF = open("/Users/billli/Projects/Python/scripts/clas/sorted.txt", "w")

all_lines = inF.readlines()
all_lines.sort()
for line in all_lines:
    outF.write(line)
