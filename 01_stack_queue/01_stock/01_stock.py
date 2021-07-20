def solution(prices):
    # answer = 몇 초 후 가격이 떨어지는지 저장
	# for i in range 값이 i에 들어간다 
	# range(len(prices)) => 0 1 2 3 4  		
    answer = [len(prices)-i-1 for i in range(len(prices))]
    # prices의 길이가 5이므로 
    # i = 0 ; 5 -0 -1 = 4
	# i = 1 ; 5 -1 -1 = 3
    # ...
    # answer = [4, 3, 2, 1, 0]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
	# i 1 2 3 4 
    for i in range(1, len(prices)):
        # stack에 값이 있는 동안
        while stack:
			# stack[-1] -> 스택의 마지막 값 
            # index = 0
            index = stack[-1]
            
			 
            # prices[0] > prices[1] 
            if prices[index] > prices[i]:
                # 0번 값이 1번 값보다 크면 가격이 떨어졌으니 answer에 값 변경
			
                answer[index] = i - index
				# stack의 마지막 값 뽑아감 
                # 떨어진 것 뽑아감
                stack.pop()
            
            # 떨어지지 않았다면 다음으로 넘어감 
            else:
                break
          	
        stack.append(i)
     # i = 1, stack = [0], answer = [4, 3, 2, 1, 0] -> stack[0, 1], answer = [4, 3, 2, 1, 0] 
     # i = 2, stack = [0,1], answer = [4, 3, 2, 1, 0] -> stack[0, 1, 2], answer = [4, 3, 2, 1, 0]
     # i = 3, stack = [0, 1, 2],  answer = [4, 3, 2, 1, 0] -> answer = [4, 3, 1, 1, 0], stack = [0, 1] -> stack [0, 1, 3]
     # i = 4, stack = [0, 1, 3], answer = [4, 3, 1, 1, 0] -> stack = [0, 1, 3, 4], answer = [4, 3, 1, 1, 0]
        
        
    return answer
    
    
   
    
    