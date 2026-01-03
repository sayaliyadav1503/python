s = "sayali"
rev1 = s[::-1]
print(rev1)

#reversed from 3rd character

S = "sayalii"
rev=S[:2]+S[2:][::-1]
print(rev)

#using loop

s="python"
rev2=" "
for i in s:
    rev2=i+rev2
print(rev2)