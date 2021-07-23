# Picking Things at Random

from math import radians
import random
values = [1,2,3,4,5,6]
print(random.choice(values))

print(random.sample(values,2))
print(random.shuffle(values))
print(random.randint(0,10))
print(random.random())

print(random.getrandbits(200))
print(random.seed())
print(random.seed(12345))
print(random.seed(b'bytedata'))
