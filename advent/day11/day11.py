file = open("input.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()


def solution_one():
    map = []
    flashes = 0
    for i in range(len(lines)):
        temp = [int(i) for i in list(lines[i].rstrip())]
        map.append(temp)
    for _ in range(9000):
        for i in range(10):
            for j in range(10):
                map[i][j] += 1
        exploded = []
        for i in range(10):
            exploded.append([False for _ in range(10)])
        while True:
            for i in range(10):
                for j in range(10):
                    if map[i][j] > 9:
                        map[i][j] = 0
                        exploded[i][j] = True
                        flashes += 1
                        if i > 0 and not exploded[i-1][j]:
                            map[i-1][j] += 1
                        if i > 0 and j > 0 and not exploded[i-1][j-1]:
                            map[i-1][j-1] += 1
                        if i > 0 and j < 9 and not exploded[i-1][j+1]:
                            map[i-1][j+1] += 1
                        if j > 0 and not exploded[i][j-1]:
                            map[i][j-1] += 1
                        if j < 9 and not exploded[i][j+1]:
                            map[i][j+1] += 1
                        if i < 9 and not exploded[i+1][j]:
                            map[i+1][j] += 1
                        if i < 9 and j > 0 and not exploded[i+1][j-1]:
                            map[i+1][j-1] += 1
                        if i < 9 and j < 9 and not exploded[i+1][j+1]:
                            map[i+1][j+1] += 1
            flag = True
            for i in range(10):
                for j in range(10):
                    if map[i][j] > 9:
                        flag = False
            if flag:
                break
        flag = True
        for i in range(10):
            for j in range(10):
                if map[i][j] != 0:
                    flag = False
        if flag:
            print(_+1)
            break

solution_one()
