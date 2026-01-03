#while loop
i=1
while i<6:
    print(i)
    i+=1
print("\n")

#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("\n")

#for loop
for i in range(1,6):
   print(i)
print("\n")

#even no
for i in range(1,11):
   if i%2==0:
      print(i)  
print("\n") 

sum = 0
for i in range(1, 6):
    sum += i
print(sum)
print("\n")

#count of character
name="sayali"
count=0
for ch in name:
   count+=1
print(count)
print("\n")

#star pattern
""" *
   **
  *** """

for i in range(1,6):
   print("*"*i)
print("\n")

#break statement
for i in range(1,6):
   if i==3:
      break
   print(i)
print("\n")
   
#nested for loop
for i in range(1,4):
   for j in range(1,3):
      print(i,j)
print("\n")

#for-else loop
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")