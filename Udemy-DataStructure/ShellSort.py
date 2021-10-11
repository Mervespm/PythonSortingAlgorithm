
array = [1,-5,6,45,32,-14]
n = len(array)

gap = int(n/2)

while gap > 0:

	for i in range(gap,n):

		temp = array[i]
		j = i

		while j >= gap and array[j-gap] > temp:

			array[j] = array[j-gap]
			j -= gap
			print(array)
		array[j] = temp
	    
	gap = int(gap / 2)


print(array)