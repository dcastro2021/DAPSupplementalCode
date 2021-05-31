#Math Module, multiplying by pi.

import math

def multiply_by_pi(a):
    x=a*math.pi
    return x

print ("Multiplying by pi")
n = input('What do you want to multiply by pi?:')
d = int(n)


c = multiply_by_pi(d)

print(c)
