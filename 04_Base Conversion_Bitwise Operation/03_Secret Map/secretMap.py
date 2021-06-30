def solution(n, arr1, arr2):
    answer = []    
    
    for i in range(n):
        bit = 0
        numBit = 0
        bit = bin(arr1[i] | arr2[i])
        numBit = bit[2:]
        b = numBit.zfill(n)
        c = []
        for i in range(n):
            if b[i] == '1':
                c.append('#')
            else:
                c.append('@')
        d = ('').join(c)
        answer.append(d.replace('@',' '))
