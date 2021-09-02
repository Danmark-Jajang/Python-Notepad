array = [1,2,3,4,5,6,7,8,9,0]
print(array)

print(array[0:3])
array[1] = -2
print(array[0:3])

array.append(11)
print(array)

array.insert(4, -4)
print(array)

array.pop(4)
print(array)

del array[3]
print(array)

del array[0:3]
print(array)

array.remove(0)
print(array)

array.clear()
print(array)