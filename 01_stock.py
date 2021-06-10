def solution(prices):
    # answer = 몇 초 후 가격이 떨어지는지 저장
	# for i in range 값이 i에 들어간다 
	# range(len(prices)) => 0 1 2 3 4  
	# i = 0 ; 5 -0 -1 = 4
	# i = 1 ; 5 -1 -1 = 3
	
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
	# i 1 2 3 4 
    for i in range(1, len(prices)):
        while stack:
			#스택의 마지막 값 
            index = stack[-1]
            
            # 주식 가격이 떨어졌다면
			# 인덱스 0 vs 인덱스 1 
            if prices[index] > prices[i]:
				#answer 0 = 1 - 0 => 1초만에 떨어졌다 
                answer[index] = i - index
				#stack의 마지막 값 뽑아감 
                stack.pop()
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
		# 1 추가 
        stack.append(i)
        
    return answer