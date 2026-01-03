#append for add item in list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert() add item in specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend() concat to list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove() remove the item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() remove specific index item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del remove specific index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear all list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#square of number
nums = [1, 2, 3, 4, 5]
result = [x*x for x in nums]
print(result)

#even number
nums = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in nums if x % 2 == 0]
print(evens)

#convert string into upper
names = ["python", "java", "html"]
caps = [name.upper() for name in names]
print(caps)

#lenght
words = ["apple", "banana", "kiwi"]
lengths = [len(word) for word in words]
print(lengths)

#replace odd with 0
nums = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else 0 for x in nums]
print(result)

#comman
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]
print(common)

#nested
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
print(flat)



