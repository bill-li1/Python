# open file with company names and positions
inF = open("/Users/billli/Projects/Python/scripts/clas/input.txt", "r")
outF = open("/Users/billli/Projects/Python/scripts/clas/output.txt", "w")

all_lines = inF.readlines()
for line in all_lines:
    if line.startswith("Incorrect"):
        continue
    elif line.startswith("The correct answer was"):
        line = line[23::]
    else:
        line = line.strip()
        line = line + " "
    outF.write(line)
