from collections import deque
file = open("input.txt", "r")
lines = file.readlines()

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points_two = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def solution_one():
    total = 0
    for line in lines:
        line = line.rstrip()
        stack = deque()
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char != pairs[stack.pop()]:
                total += points[char]
    print(total)

def solution_two():
    answers = []
    for line in lines:
        total = 0
        line = line.rstrip()
        stack = deque()
        flag = True
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char != pairs[stack.pop()]:
                flag = False
        if flag:
            while stack:
                top = pairs[stack.pop()]
                total *= 5
                total += points_two[top]
            answers.append(total)
    answers.sort()
    print(answers[len(answers)//2])

solution_two()
