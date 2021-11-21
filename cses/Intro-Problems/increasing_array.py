n = int(input())
s = [int(x) for x in input().split()]
total = 0
l = s[0]
for num in s:
    if num < l:
        total += l - num
    l = max(l, num)
print(total)
