
for i in range(1,5):
    print("*" * i)
print("\n")

#square
n=10
for i in range(n):
      print("*" *n)
print("\n")

#inverted
s=5
for i in range(s,0,-1):
      print("*"*i)
print("\n")

#piramid
n=10
for i in range(1,n):
      print(" " * (n-i) + "*" * (2*i-1))
print("\n")

#inverted piramid   
n=10
for i in range(n,0,-1):
      print(" " * (n-i) + "*" * (2*i-1))    
print("\n")

n=4
for i in range(1,n):
      print(" " * (n-i) + "*" * (2*i-1)) 
for i in range(n,0,-1):
      print(" " * (n-i) + "*" * (2*i-1)) 