def solution(progresses, speeds):
    answer = [0]
    index = 0
    while progresses:
        while progresses[0] < 100:
            for i in range(0, len(progresses)):
                progresses[i] = progresses[i] + speeds[i]
                
        progresses.pop(0)
        speeds.pop(0)
        answer[index] = answer[index] + 1
        
        if progresses:
            if progresses[0] < 100:
                answer.append(0)
                index = index + 1
            
    return answer