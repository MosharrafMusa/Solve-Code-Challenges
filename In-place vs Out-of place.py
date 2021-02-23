# in-place

array = ['a', 'b', 'c', 'd']

print("Before", array)

lenght = len(array) - 1

for i in range(lenght // 2 + 1):
    #print("Swapping", array[i], 'and', array[lenght - i])

    tmp = array[i]
    array[i] = array[lenght - i]
    array[lenght - i] = tmp

print("After", array)


# out-in place:
array = ['a', 'b', 'c', 'd']
new_array = ['a'] * len(array)

print("Before", array)

lenght = len(array) - 1

for i in range(lenght):
    new_array[i] = array[lenght - i]

array = new_array
print("After", array)
