# 딕셔너리를 이용한 방법 
def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in completion:
        if hash[i]==1:
            del hash[i]    
        else:
            hash[i]-=1
    return list(hash.keys())[0]