# data structre in python 

# list data structure

list_item = ["list_item1", "list_item2", "ect..."] 

print(list_item)

print(list_item[0])

print(list_item[-1])


# Postive indexes (0,1,2,3,4,5,6,7,8,9)

# Negetive indexes (-1,-2,-3,-4,-5,-6,-7,-8,-9)

# changing the lsit by index value

list_item[0] = "change the value"
print(list_item)

# adding the list element at the end

list_item.append("list_item_03")

print(list_item)

# adding the list of elementf at the end

list_item.extend(["list_item_04", "list_item_05"])

print(list_item)


# An example that uses most of the list methods:

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')
print(fruits.count('apple'))
print(fruits)

fruits.count('tangerine')
print(fruits)

fruits.index('banana')
print(fruits)

fruits.index('banana', 4)  # Find next banana starting at position 4
print(fruits)

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

