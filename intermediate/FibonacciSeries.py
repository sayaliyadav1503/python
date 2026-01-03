def fibbo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibbo(10)

n=int(input("enter no:"))
a,b=0,1
print("fabbo series")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

