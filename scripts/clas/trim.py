# open file with company names and positions
inF = open("/Users/billli/Projects/Python/scripts/clas/test.txt", "r")
outF = open("/Users/billli/Projects/Python/scripts/clas/final.txt", "w")

all_lines = inF.readlines()
sorted_lines = []
for i in range(len(all_lines)):
	if i%2==0:
		line = all_lines[i].strip() + " | " + all_lines[i+1]
		sorted_lines.append(line)

sorted_lines.sort()
for line in sorted_lines:
	outF.write(line)
