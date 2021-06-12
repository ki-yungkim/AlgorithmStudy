def solution(bridge_length, weight, truck_weights):
    answer = 0
    position = [0] * bridge_length
    
    while position:
        answer += 1
        position.pop(0)
        if truck_weights:
            if truck_weights[0] + sum(position) <= weight:
                position.append(truck_weights.pop(0))
            else:
                position.append(0)
        
    
    return answer