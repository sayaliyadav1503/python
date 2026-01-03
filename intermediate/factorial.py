def cal(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

n=int(input("enter your number:"))
factorial=cal(n)
print("factorial of: ",n,"is:",factorial)