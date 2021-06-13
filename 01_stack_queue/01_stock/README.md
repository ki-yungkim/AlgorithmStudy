# Algorithm_Step1_Stack_Queue
## 1번 주식 문제
***

### 문제 설명 
- 초 단위로 기록된 주식가격이 담긴 배열 prices
- 가격이 떨어지지 않고 버티는 시간을 반환합니다.

### 제한사항
- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

### 입출력 예시 
 | prices          |
 | :-------------- |
 | [1, 2, 3, 2, 3] |

 | return          |
 | :-------------- |
 | [4, 3, 1, 1, 0] |

#### 설명  
- 1초 기준 가격 1은 마지막 5초 시점까지 떨어지지 않는다 => 4초 동안 유지
- 2초 기준 가격 2는 마지막 5초 시점까지 떨어지지 않는다 => 3초 동안 유지
- 3초 기준 가격 3은 4초에 떨어진다 			  => 1초 동안 유지
- 4초 기준 가격 2는 마지막 5초 시점까지 떨어지지 않는다 => 1초 동안 유지
- 5초 기준 가격 3은 마지막이라 				  => 0초 유지

### 코드 구조 구상

- 스택 prices의 인덱스 0부터 추가 
- 새로운 주가가 들어왔을 때 마지막에 넣었던 주가와 비교한다
- 떨어지지 않았다면 다음 주가를 넣고 비교한다 
- 떨어지면 스택에서 값 빼기 
- for 1초부터 4초까지 
- while stack에 값 다 없어지면 끝 
- 기준 < 새로운거 

### 코드 구현

<pre>
<code>
	def solution(prices):
	
		# answer = 몇 초 후 가격이 떨어지는지 저장 [ ]
		# for i in range 값이 i에 들어간다 
		# range(len(prices)) => 0 1 2 3 4  
		# i = 0 ; 5 -0 -1 = 4
		# i = 1 ; 5 -1 -1 = 3
		
		answer = [len(prices) - i - 1 for i in range(len(prices))]
		
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
				
				# 떨어지지 않았다면 다음 시점으로 넘어감 
				else:
					break
			
			# 스택에 추가한다
			# 1 추가 
			stack.append(i)
			
		return answer

</code>
</pre>
