#current date and time
from datetime import datetime
now = datetime.now()
print(now)
print("\n")

#current date
from datetime import date
today = date.today()
print(today)
print("\n")

#access day,month,year
today = date.today()
print(today.day)
print(today.month)
print(today.year)
print("\n") 

#custom date
d = date(2024, 12, 25)
print(d)
print("\n")

#diff bitween two dates
d1 = date(2024, 1, 1)
d2 = date(2024, 1, 10)
diff = d2 - d1
print(diff.days)
print("\n")

#format date
now = datetime.now()
print(now.strftime("%d-%m-%Y"))
print("\n")

import math

#square root
print(math.sqrt(25))
print("\n")


print(math.pow(2, 3))    
print(math.floor(3.7))  
print(math.ceil(3.2))
print("\n") 

#factorial
print(math.factorial(5))
print("\n")

#trignometric function
print(math.sin(math.radians(90)))
print("\n")