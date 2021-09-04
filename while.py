import time

number  = 0
target_tict = time.time() + 5

while target_tict > time.time():
    number += 1

print("5sec : {}".format(number))