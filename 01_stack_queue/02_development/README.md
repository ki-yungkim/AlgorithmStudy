# Algorithm_Step1_Stack_Queue
# 2번 기능개발 문제
***

### 문제 설명 
- 기능은 진도가 100% 일때 서비스에 반영 가능
- 각 기능의 개발 속도는 모두 다름 
- 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능
- 이 경우에 뒤에 있는 기능은 앞 기능 배포될 때 같이 배포 
- 배포는 하루 한번, 하루의 끝에 배포 
- ex) 95%, 속도 4 => 99% => 100% -> 2일 뒤 배포 

### 제한사항


### 입출력 예시 
 | progresses   |  | speeds       | | retrun       |  
 | :----------- |  | :----------- | | :----------- |
 | [90, 30, 55] |  | [1, 30, 5]   | | [2, 1]       |

 | progresses               |  | speeds             | | retrun       |  
 | :-----------             |  | :-----------       | | :----------- |
 | [95, 90, 99, 99, 80, 99] |  | [1, 1, 1, 1, 1, 1] | | [1, 3, 2]    |
 

#### 예시 설명  
- 90 : 배포일 7일 후
- 30 : 배포일 완성은 3일 후, 앞 순서와 같이 배포되서 7일 후  
- 50 : 배포일 9일 후
- 7일 후 2개, 9일 후 1개 => [2, 1]


### 코드 구조 구상

- progresses의 각 요소에 speeds의 요소 더하기 이걸 반복
- progresses의 0번 요소 값이 100 이상이 되면 pop(0) 하고
- answer의 0번에 1 추가 
- while문으로 반복 0번 요소 값이 100 미만일 때까지
- 없으면 answer의 1번으로 넘어가서 다시 추가 

### 코드 구현

<pre>
<code>
	def solution(progresses, speeds):
        answer = []
        stack = 0
        while progressess:

		while progresses[0] < 100: 
			for i in range((0, len(progresses)):
				progresses[i] + speeds[i]
                
		progresses.pop(0)
		speeds.pop(0)
		answer[stack] = answer[stack] + 1
		if progresses[0] < 100:
			stack = stack + 1
		
	return answer

</code>
</pre>
