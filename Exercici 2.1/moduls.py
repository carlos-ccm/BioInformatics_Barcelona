#math.py
import math
#90 graus a radians
print("90 graus son: ",math.radians(90),"radians")

#sinus de 45 graus
angle_in_radians = math.radians(45)
print(f"{math.sin(angle_in_radians):.2f}")

#arrodoneix pi
print("Pi arrodonit al numero sencer superior:",math.ceil(math.pi))
print("Pi arrodonit al numero sencer inferior:",math.floor(math.pi))

#random.py
import random

print("Numero random entre 0 y 1:",random.uniform(0,1))
print("Numero random entre 0 y 10:",random.uniform(0,10))
print("Numero random entre 0 y 10:",random.randint(0,10))
print("Numero random entre 0 y 1:",random.gauss(3,1)) #3 seria la mitja

#sys.py
import sys

print(sys.argv)