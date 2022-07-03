from collections import deque

file = open("input.txt", "r")
map = file.readlines()

def solution_one():
    count = 0
    
    for i in range(len(map)):
        map[i] = map[i][:len(map[i])-1]
    
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] != '\n' and not ((row > 0 and map[row][col] >= map[row-1][col]) or
                (col > 0 and map[row][col] >= map[row][col-1]) or
                (row < len(map) - 1 and map[row][col] >= map[row+1][col]) or
                (col < len(map[row]) - 1 and map[row][col] >= map[row][col+1])):
                count += int(map[row][col]) + 1
    print(count)

def solution_two():
    start_rows = []
    start_cols = []
    for i in range(len(map)):
        map[i] = map[i][:len(map[i])-1]
    
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] != '\n' and not ((row > 0 and map[row][col] >= map[row-1][col]) or
                (col > 0 and map[row][col] >= map[row][col-1]) or
                (row < len(map) - 1 and map[row][col] >= map[row+1][col]) or
                (col < len(map[row]) - 1 and map[row][col] >= map[row][col+1])):
                start_rows.append(row)
                start_cols.append(col)
    
    max = []
    visited = []
    for i in range(len(map)):
        visited.append([])
        for _ in range(len(map[i])):
            visited[i].append(False)
    for pos in range(len(start_rows)):
        rowq = deque([start_rows[pos]])
        colq = deque([start_cols[pos]])
        members = []
        count = 1
        while rowq:
            row = rowq.popleft()
            col = colq.popleft()
            members.append(map[row][col])
            visited[row][col] = True
            if row > 0 and map[row][col] < map[row-1][col] and not visited[row-1][col] and map[row-1][col] != '9':
                members.append(map[row-1][col])
                count += 1
                rowq.append(row-1)
                colq.append(col)
                visited[row-1][col] = True
            if col > 0 and map[row][col] < map[row][col-1] and not visited[row][col-1] and map[row][col-1] != '9':
                members.append(map[row][col-1])
                count += 1
                rowq.append(row)
                colq.append(col-1)
                visited[row][col-1] = True
            if row < len(map) - 1 and map[row][col] < map[row+1][col] and not visited[row+1][col] and map[row+1][col] != '9':
                members.append(map[row+1][col])
                count += 1
                rowq.append(row+1)
                colq.append(col)
                visited[row+1][col] = True
            if col < len(map[row]) - 1 and map[row][col] < map[row][col+1] and not visited[row][col+1] and map[row][col+1] != '9':
                members.append(map[row][col+1])
                count += 1
                rowq.append(row)
                colq.append(col+1)
                visited[row][col+1] = True
        max.append(count)

        # add functionality to check visited

    count = 1
    max.sort(reverse=True)
    for i in range(3):
        count *= max[i]
        
    print(count)




solution_two()
