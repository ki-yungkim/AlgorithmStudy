import sys
from collections import deque 

def facto(n):
    r = 1
    for i in range (1, n+1):
        r *= i
    return r


while True:
    try:
        digit=deque()
        n = sys.stdin.readline().rstrip()
      
        digit = deque(map(int, list(n)))
       
        length = len(digit) 
        result = 0
        while digit:
            result +=  facto(length) * digit.popleft() 
             
            length -= 1
        if result != 0:
            print(result)
        
    except:
        break