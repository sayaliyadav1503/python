#set remove duplicate
nums = {1, 2, 2, 3, 3, 4}
print(nums)

#create set from list
lst = [10, 20, 20, 30]
s = set(lst)
print(s)

#add element
s = {1, 2}
s.add(3)
print(s)

#remove element
s = {1, 2, 3}
s.remove(2)
print(s)

#union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

#intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

#diff
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)

#set compression
nums = [1, 2, 3, 4, 5]
squares = {x*x for x in nums}
print(squares)