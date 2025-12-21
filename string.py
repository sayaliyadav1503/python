#finds array no.
string = "sayaliyadav"
print(string[2],"\n")

#for loop for string
for x in "banana":
      
      print(x)
print("\n")

#finds lenght of String
print(len(string))
print("\n")

#if Statement
txt="im free right know...."
if "free" in txt:
      print("yes,'free'is present")
print("\n")

#slicing
a="sayali yadav"
print(a[1:5])
print(a[7:])
print(a[:7])
print("\n")

#upperCase
print(a.upper())
print(a.lower())
print(a.strip())
print(a.capitalize())
print(a.replace("s","p"))
print("\n")

#concatenate
a="ganpati "
b="bappa"
c=a+b
print(c)
print("\n")

#formateString/escape caracter
age = 36
txt = f"My name is John, I am \"{age}\"" 
print(txt)
t=f"i am sayali and my age is \"{3*7}\""
print(t)