def solution(answers):
    answer = []
    score = [0, 0, 0]
    a = [1,2,3,4,5] 
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            score[0] += 1
        if b[i%len(b)] == answers[i]:
            score[1] += 1
        if c[i%len(c)] == answers[i]:
            score[2] += 1
    
    for i in range(0, len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer