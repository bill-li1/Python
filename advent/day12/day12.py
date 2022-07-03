import copy, collections

file = open("test.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()

"""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

def solution_two():
    m = collections.defaultdict(set[str])
    for line in lines:
        src, dest = line.split('-')
        m[src].add(dest)
        m[dest].add(src)
    todo: list[tuple] = [(True, ('start',))]
    allpaths = set()
    while todo:
        double_move, path = todo.pop()
        if path[-1] == 'end':
            allpaths.add(path)
            continue
        for neighbor in m[path[-1]]:
            if neighbor == 'start':
                continue
            if neighbor.isupper() or neighbor not in path:
                todo.append((double_move, (*path, neighbor)))
            elif double_move:
                todo.append((False, (*path, neighbor)))
    print(len(allpaths))
solution_two()


#dfs
def dfs_solution():
    m = collections.defaultdict(set[str])
    for line in lines:
        f, t = line.split("-")
        m[f].add(t)
        m[t].add(f)
    todo: list[tuple] = [("start",)]
    allpaths = set()
    while todo:
        path = todo.pop()
        if path[-1] == "end":
            allpaths.add(path)
        for neighbor in m[path[-1]]:
            if neighbor.isupper() or neighbor not in path:
                todo.append((*path, neighbor))
        
    print(len(allpaths))
        
def bfs_solution(): 
    m = collections.defaultdict(set[str])
    for line in lines:
        s, f = line.split("-")
        m[s].add(f)
        m[f].add(s)
    todo: collections.deque[tuple] = collections.deque([("start",)])
    allpaths = set()
    while todo:
        path = todo.popleft()
        if path[-1] == "end":
            allpaths.add(path)
        for neighbor in m[path[-1]]:
            if neighbor.isupper() or neighbor not in path:
                todo.append((*path, neighbor))


def dfs(current: str, visited: dict[str, bool], paths: dict[str, list[str]]) -> int:
    newList = copy.deepcopy(visited)
    if current == "end": 
        return 1
    if current.islower():
        newList[current] = True
    total = 0
    for i in paths[current]:
        if not newList[i]:
            total += dfs(i, newList, paths)
    return total



def solution_one():
    m = {}
    v = {}

    for line in lines:
        f = line[:line.find("-")]
        t = line[line.find("-")+1:]
        v[f] = False
        v[t] = False
        if f in m:
            m[f].append(t)
        else:
            m[f] = [t]
        if t in m:
            m[t].append(f)
        else:
            m[t] = [f]
    print(dfs("start", v, m))
    print(v)
