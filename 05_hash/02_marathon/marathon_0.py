# Counter를 이용한 방법
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]