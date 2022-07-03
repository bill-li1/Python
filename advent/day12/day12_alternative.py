from collections import defaultdict

file = open("test.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()

def solution_one():
    map = defaultdict(list)
    for line in lines:
        f, t = line.split("-")
        
    
