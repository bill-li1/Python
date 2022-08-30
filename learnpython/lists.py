# lists
mylist = [1, 2, 3]

# accessing items
myitem = mylist[1]  # access item at index
lastitem = mylist[-1]  # access items from the back of a list

# basic list functions with regards to a single item in the list
mylist.append(4)  # add items to end of list
mylist.insert(0, 0)  # add items elsewhere in list
lastitem = mylist.pop()  # pops last item (returns item)
firstitem = mylist.pop(0)  # pops item (returns item)
mylist.remove(2)  # removes first instance of item (does not return item)

# basic list functions that pertain to the entire list object
mylist.reverse()  # reverse a list
mylist.sort()

# check if item is in list
if 1 in mylist:
    print("1 is in the list")

# iterate through a list
for elm in mylist:
    print(elm)


# removes all instances of item from list
def removeAllInstances(mylist: list, val: int) -> list:
    return [item for item in mylist if item != val]


def addOne(mylist: list) -> list:
    mylist = mylist
    mylist.append(2)  # [1]
