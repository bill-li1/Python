n = int(input())
total = n*(n+1)//2
if total%2 == 1:
    print("NO")
    quit()
goal = total//2
l1 = []
l2 = []
for i in range(n, 0, -1):
    if i <= goal:
        l1.append(i)
        goal -= i
    else:
        l2.append(i)
print("YES")
print(len(l1))
for i in l1:
    print(i, end=' ')
print(f"\n{len(l2)}")
for i in l2:
    print(i, end=' ')
