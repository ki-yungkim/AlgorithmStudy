import sys

def binary(n):
    if n > 1:
        binary(n//2)
        
    if n % 1 == 1:
        print(0, end = "")
    
    else:
        print(0, end = "")

n = sys.stdin.readline()
binary(int(n))