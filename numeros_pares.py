#!/usr/bin/env python3

#usando while
'''
num = 1
while num <= 200:
    if num % 2 != 0:
        num += 1
        continue
    print(num)
    num += 1
'''

#usando for
for num in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)
