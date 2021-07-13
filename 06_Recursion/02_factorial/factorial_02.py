import sys

def factorial(n):

  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return n * factorial(n-1)
    
n = sys.stdin.readline()
print(factoral(int(n)))