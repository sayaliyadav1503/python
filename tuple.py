#tuple is immutable
t = (10, 20, 30)
print(t)

#unpack
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

#tuple in loop
t = (10, 20, 30)
for item in t:
    print(item)

#swap
a = 5
b = 10
a, b = b, a
print(a, b)

#count and index method
t = (1, 2, 3, 2, 2)
print(t.count(2))
print(t.index(3))

#tuple inside list
students = [("Amit", 85), ("Neha", 90), ("Rahul", 78)]
for name, marks in students:
    print(name, marks)