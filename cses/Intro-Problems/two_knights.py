n = int(input())
for k in range(1, n+1):
    print(k*k*(k*k-1)//2-4*(k-2)*(k-1) if k > 2 else (k*k*(k*k-1)//2))
