
array = [-9,6,14,-11,15,69]

n = len(array)

for i in range(n):
    min_index = i

    for j in range(i+1,n):

        if array[j] < array[min_index]:
            min_index = j

    array[min_index], array[i] = array[i], array[min_index]

print(array)

