s = input()
m_start = s.count('L')
s_start = m_start + s.count('M')
ml = s[m_start:s_start].count('L')
ms = s[m_start:s_start].count('S')
sl = s[s_start:].count('L')
sm = s[s_start:].count('M')
count = 0
for c in s[:m_start]:
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
