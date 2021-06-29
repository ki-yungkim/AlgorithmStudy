
import math 
import sys
while True:
    n = sys.stdin.readline().rstrip()  
    length = len(n)
      
    result = 0
        
    if n == '0':
        break
            
    for i in range(length):
        result += int(n[i])* math.factorial(length - i)
            
    print(result)    
   