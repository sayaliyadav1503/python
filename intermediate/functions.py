def add(a,b):
  return a+b
print(add(3,5))
print("\n")

#without return function
def greet(name):
  print("hello",name)
greet("sayali")
print("\n")

def greet(name="User"):
    print("Hello", name)

greet()
greet("Riya")
print("\n")


#keyword arg
def student(name,surname):
  print(name,surname)
student(name="sayali",surname="yadav")
print("\n")


#variable length
def add(*nums):
  total=0
  for n in nums:
    total +=n
  return total
print(add(1,2,3,4))
print("\n")

#lambda function
square = lambda x: x * x
print(square(5))
print("\n")

#double all number in list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
print("\n")

#factorial no
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
print("\n")


#fibonacci series
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
print("\n")
