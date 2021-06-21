a = int(input()) # takes input on 2 different lines, different from c++
b = int(input())

print(f'The value of a is {a} and the value of b is {b}') # similar to 

def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result)) 
# map returns map object, an iterator that yields items on demand
# this is why we call list(result)
# same as c and js map, but the function comes first, 
# and the array being mapped comes second,

x, y = map(int, input().split())
print(f'The value of x is {x} and the value of y is {y}') # similar to 
# this takes 2 input on one line

n, m = [int(x) for x in input().split()]
print(f'The value of n is {n} and the value of m is {m}') # similar to 

