# 내 최선이지만 시간 초과
def solution(participant, completion):
    participant.sort()
    completion.sort()
    x = 0
    for i in range(len(participant)-1):
        if participant[i] == participant[i+1]:
            x = participant.pop(i)
            participant.append(x) 
    
    
    while completion:
        i = 0;
        if participant[i] == completion[i]:
            participant.pop(0)
            completion.pop(0)
    return participant[0]