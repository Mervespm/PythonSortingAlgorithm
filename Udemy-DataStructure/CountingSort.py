
# If you're doing much numerical work with arrays like this, I'd suggest numpy, which comes with a cumulative sum function cumsum:

import numpy as np

array = [1,0,3,1,3,1]

freq = []
for i in range(0, max(array)+1 ):
	freq.append(array.count(i))

for i in range(1,4):
	freq[i] = freq[i-1]+ freq[i]

freq[0] = 0

for i in range(len(array)):
	






