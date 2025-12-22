dict1={
       "name":"sayali",
       "age":23,
       "education":"MCA"

}
print(dict1)
print(dict1["age"])
print(len(dict1))
print(type(dict1))
x=dict1.get("education")#another method of print the value
print(x)
y=dict1.keys()#gets key
print(y)
z=dict1.values()
print(z)

#constructor
dictionary= dict(name="sayali",age="23")
print(dictionary)

#for add key:value pair in dictionary[update]
dict1["surname"]="yadav"
print(dict1)
dict1.update({"city":"pune"})#another method for update
print(dict1)

#pop() to remove
dict1.pop("age")
print(dict1)

#popitem() remove last insertion item
dict1.popitem()
print(dict1)

#del() delete specific item
del dict1["surname"]
print(dict1)

#clear() to clear dictionary
dict1.clear()
print(dict1)

#nested loop in dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

#without using loop
child1={
       "name":"sayali",
       "surname":"yadav"
      },
child2={
       "name":"amisha",
       "surname":"patil"
      },
child3={
       "name":"monika",
       "surname":"isave"
      }
myfam = {
       "child1":child1,
       "child2":child2,
       "child3":child3
       }
=======
dict1={
       "name":"sayali",
       "age":23,
       "education":"MCA"

}
print(dict1)
print(dict1["age"])
print(len(dict1))
print(type(dict1))
x=dict1.get("education")#another method of print the value
print(x)
y=dict1.keys()#gets key
print(y)
z=dict1.values()
print(z)

#constructor
dictionary= dict(name="sayali",age="23")
print(dictionary)

#for add key:value pair in dictionary[update]
dict1["surname"]="yadav"
print(dict1)
dict1.update({"city":"pune"})#another method for update
print(dict1)

#pop() to remove
dict1.pop("age")
print(dict1)

#popitem() remove last insertion item
dict1.popitem()
print(dict1)

#del() delete specific item
del dict1["surname"]
print(dict1)

#clear() to clear dictionary
dict1.clear()
print(dict1)

#nested loop in dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

#without using loop
child1={
       "name":"sayali",
       "surname":"yadav"
      },
child2={
       "name":"amisha",
       "surname":"patil"
      },
child3={
       "name":"monika",
       "surname":"isave"
      }
myfam = {
       "child1":child1,
       "child2":child2,
       "child3":child3
       }
print(myfam)

#square of no.
nums = [1, 2, 3, 4]
squares = {x: x*x for x in nums}
print(squares)

#example
students = {
    "Rahul": 85,
    "Neha": 92,
    "Amit": 78
}

for name, marks in students.items():
    print(name, "scored", marks)