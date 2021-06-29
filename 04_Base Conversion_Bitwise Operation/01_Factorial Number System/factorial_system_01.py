import math 
import sys
while True:
    try:
        digit=[]
        n = sys.stdin.readline().rstrip()
      
        digit = list(map(int, list(n)))
        length = len(digit)
       
        r = 0
        result = 0
        while digit:
            result +=  math.factorial(length) * digit.pop(0)             
            length -= 1
        if result != 0:
            print(result)
        
    except:
        break