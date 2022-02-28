# -*- coding: utf-8 -*-
"""Swapping_varibles


a = 1
c = 'hello world'

print(a)
print(c)

f = a 
print(f)

a = 2
print(a)
print(f)

"""First metod to swap values of two variables """

v1 = 'first string'
v2 = 'second string'

temp1 = v1
temp2 = v2

v1 = temp2 
v2 = temp1

print(v1, v2)

"""second and more efficient method"""

v1 = 'fist string'
v2 = 'second string'

temp1 = v2

v2 = v1
v1 = temp1

print(v1, v2)
