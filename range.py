for i in range(5):
    print(i)
print("\n")

#range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
print("\n")

#reverse ordered
for i in range(5, 0, -1):
    print(i)
print("\n")

#even no
for i in range(2, 11, 2):
    print(i)
print("\n")

#convert range to list
nums = list(range(1, 6))
print(nums)
print("\n")

#length of range
r = range(1, 10, 2)
print(len(r))
print("\n")

#negative step
for i in range(10, 0, -2):
    print(i)
print("\n")

#codition
print(3 in range(1, 5))
