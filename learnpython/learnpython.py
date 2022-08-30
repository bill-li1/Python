# lists
mylist = [1, 2, 3]

# add items to end of list
mylist.append(4)

# add items elsewhere in list
mylist.insert(0, 0)

# access item at index
myitem = mylist[1]

# access items from the back of a list
lastitem = mylist[-1]

# check if item is in list
if 1 in mylist:
    print("1 is in the list")

# iterate through a list
for elm in mylist:
    print(elm)

# remove elements from a list
lastitem = mylist.pop()  # pops last item (returns item)
firstitem = mylist.pop(0)  # pops item (returns item)
mylist.remove(2)  # removes first instance of item (does not return item)


# removes all instances of item from list
def removeAllInstances(mylist: list, val: int) -> list:
    return [item for item in mylist if item != val]


# python is pass by value for immutable things
# python is pass by reference for mutable things unless you try to reasign
def redo(mylist: list):
    mylist.append("haha lol")  # caller also gets appended "haha lol"
    mylist = ["haha lol"]  # caller is the same
    print("inside", mylist)


print("---------------")
test = [1, 2, 3]
redo(test)
print("outside", test)
