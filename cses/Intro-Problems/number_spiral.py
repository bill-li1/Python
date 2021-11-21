n = int(input())
for _ in range(n):
    y, x = map(int, input().split())
    if y > x:
        if y%2 == 0:
            starty = y*y
            startx = x-1
            print(starty-startx)
        else:
            starty = (y-1)*(y-1)
            startx = x
            print(starty+startx)
    elif x > y:
        if x%2 == 1:
            startx = x*x
            starty = y-1
            print(startx-starty)
        else:
            startx = (x-1)*(x-1)
            starty = y
            print(startx+starty)
    else:
        print(x*x-x+1)
