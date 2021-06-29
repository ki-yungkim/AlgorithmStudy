from string import ascii_uppercase 

number, base = input().split(" ")
base = int(base)

digit = []
digit = list(number)

alphabet_list = list(ascii_uppercase)
numbers_list = list(range(10,36))

length = len(digit)
result = 0
nSquare = length - 1 
for i in range(length):
    index = 0
    if digit[i].isdigit():
        result += int(digit[i]) *  (base ** nSquare)
    else:
        index = alphabet_list.index(digit[i])
        result += numbers_list[index] *  (base ** nSquare)
    nSquare -= 1  

print(result)
   