print(list(range(5)))

for i in range(5):
    print(str(i)+"= repeat variable")
print()

for i in range(5, 10):
    print(str(i)+"= repeat variable")
print()

for i in range(0, 10, 2):
    print(str(i)+"= repeat variable")

ary = [3, 25, 94, 104, 73, 62]
for i in range(len(ary)):
    print("{} - {}".format(i, ary[i]))

for i in range(4, 0-1, -1): #reverse 
    print(i)
print()

for i in reversed(range(5)):
    print(i)