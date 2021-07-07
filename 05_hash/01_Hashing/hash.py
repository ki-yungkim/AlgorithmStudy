import sys
from string import ascii_lowercase

n = sys.stdin.readline() 
x = sys.stdin.readline()
x_list = list(x)
alpha_list = list(ascii_lowercase)
hash = {}
for i in range(1, 27):
    hash[alpha_list[i-1]] = i

result_sum = 0
for i in range(len(x)):
     for j in range(26):
             if x_list[i]==alpha_list[j]:
                    result = hash[alpha_list[j]]
                    result_sum += result * 31 ** i
                    result_large = result_sum%1234567891 

print(result_large)