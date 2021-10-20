def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    # 1번 집을 터는 경우 
    dp1[0] = money[0]
    # 원형으로 연결되기 때문에 1번 집을 털면 마지막 집은 털지 못한다 
    for i in range(1, len(money) - 1 ):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # 1번 집을 안 터는 경우 
    dp1[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[-2], dp2[-1])