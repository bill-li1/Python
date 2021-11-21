n = int(input())
s = n*(n+1)//2
nums = [int(x) for x in input().split()]
for num in nums:
    s -= num

print(s)
