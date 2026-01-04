lst=[1,2,1,1,1,1,2,2,2,2,2,32,3,3,4]
freq={}
for item in lst:
      freq[item]=freq.get(item,0)+1
print(freq)

