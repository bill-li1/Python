s = input()
mstart = s.count('L')
sstart = mstart + s.count('M')
ml = s[mstart:sstart].count('L')
ms = s[mstart:sstart].count('S')
sl = s[sstart:].count('L')
sm = s[sstart:].count('M')
count = 0
for c in s[:mstart]:
    if c == 'M':
        count += 1
        if ml > 0:
            ml -= 1
        else:
            ms -= 1
            sl -= 1
            count += 1
    elif c == 'S':
        count += 1
        if sl > 0:
            sl -= 1
        else:
            ml -= 1
            sm -= 1
            count += 1
print(count+sm)
