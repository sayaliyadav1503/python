list1=[2,4,5]
list2=[5,1,8]
list3=list1+list2
list3.sort()
print(list3)

list1=[1,2,3,5,6,7,8,9,3,5,6]
unique=set(list(list1))
print(list1)

nums = [1, 2, 3, 2, 4, 1, 5]

unique_nums = list(dict.fromkeys(nums))
print(unique_nums)


my_list = [1, 2, 3, 2, 4, 1, 5]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print("Original list:", my_list)
print("List without duplicates:", new_list)
