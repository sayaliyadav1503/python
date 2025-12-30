num=15
flag =True
for i in range(2,num):
    if num%2==0:
       flag=False
       break
print("prime" if flag else "not prime")

num=int(input("enter no:"))
flag=True
for i in range(2,num):
    if num%2==0:
        flag=False
        break
print("prime" if flag else "not prime")