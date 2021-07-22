
def solution(prices):
    answer = [0] * len(prices)
        #[0, 0, 0, 0, 0]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] +=1
            if prices[i] > prices[j]:
                break
                   
    return answer