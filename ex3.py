scores1 = [85.0,75.0,95.0,110.0,56.0]
scores = range(12,333,2)
count = (int)(len(scores))
print count
counter = 0
addit=0.
while (counter < count) :
  addit = addit + scores[counter]
  counter = counter + 1
print addit  
