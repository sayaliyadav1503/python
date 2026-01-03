#keep original order
#preserve order
lst=[1,2,3,3,4,4,5,5,6,6,7]
newlst=[]
for i in lst:
    if i not in newlst:
        newlst.append(i)
print("old list:",lst)
print("new list",newlst)

#order is not preserved
#set() change order in sequence
list1=[1,1,2,2,3,3,11,4,4,5,5,5,5]
unique=list(set(list1))
print(unique)

#using list compression
number=[1,2,3,4,5,3,2,1]
num=[]
[num.append(x) for x in number if x not in num]
print(num)

#dict.fromkeys() commanly use for remove duplicate
#creates a dictionary using given keys with a common value
num=list(dict.fromkeys(number))
print(num)


