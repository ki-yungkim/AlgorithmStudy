from sys import stdin
from collections import Counter

a = stdin.readline()
b = stdin.readline().split()
c = stdin.readline()
d = stdin.readline().split()

C = Counter(b)

for i in d:
    if i in C:
        print(f'{C[i]}', end=' ')
    else: 
        print('0', end=' ')