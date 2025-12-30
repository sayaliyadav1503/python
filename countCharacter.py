s="sayali"
count={}
for ch in s:
       count[ch]=count.get(ch,0)+1
print(count)

#with user input
string=input("enter string:")
count={}
for ch in string:
       count[ch]=count.get(ch,0)+1
print(count)