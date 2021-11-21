s = input()
longest = 0
current = 0
before = s[0]
for x in s:
    if x != before:
        longest = max(longest, current)
        before = x
        current = 1
    else:
        current += 1

print(max(longest, current))
