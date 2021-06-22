  
import random
r = [random.randint(-100, 100) for x in range(30)]
largest_number = max(r)
r.index(largest_number)
print(r)
print(largest_number)
print(r.index(largest_number)+1)
for i in range(29):
  if r[i]<0 and r[i+1]<0:
    print(r[i],r[i+1])
