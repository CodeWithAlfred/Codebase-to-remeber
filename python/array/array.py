import array as arr
array_data = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Looping through an array
print('\n \t Looping through an array ')
for num in array_data:
    print(num)


# appending to an array
print('\n \t Adding.appenging elements')
array_data.append(11)
print(array_data)


# extending to ana array (Adding multiple data)
array_data.extend([12, 13, 14, 15])
print(array_data)


# Inserting to an array
array_data.insert(2, 25)
print(array_data)


# REMOVING ELEMENTS FROM ARRAYS USING POP() AND REMOVE()
# pop() removes an element from the end of the array o at specific index if spplied as argument
print('\n\t REMOVING ELEMENTS FROM AN ARRAY \n')
print('Popping last element', array_data.pop())
print(array_data)


# remove() removes a specific element without printing it out unlike pop()

array_data.remove(4)
print(array_data)


# Array concatination
a = arr.array('f', [1, 2, 3, 4, 5])
b = arr.array('f', [6, 7, 8, 9, 10])

c = a+b
print('\n array c is equal to: ', c)
