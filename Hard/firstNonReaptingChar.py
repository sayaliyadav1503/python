string = input("Enter a string:")
for char in string:
    if string.count(char)==1:
        print("first non-repeating character",char)
        break
    else:
        print("no non-repeating character found")