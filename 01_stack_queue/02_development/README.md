# Algorithm_Step1_Stack_Queue
## 2번 기능개발 문제
***

### 문제 설명 
- 기능은 진도가 100% 일때 서비스에 반영 가능
- 각 기능의 개발 속도는 모두 다름 
- 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 완료 가능
- 이 경우에 뒤에 있는 기능은 앞 기능 배포될 때 같이 배포 
- 배포는 하루 한번, 하루의 끝에 배포 
- ex) 95%, 속도 4 => 99% => 100% -> 2일 뒤 배포 

### 제한사항
- 작업의 개수(progresses, speeds 배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 

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
- stack으로 answer의 요소 번호 관리 
- progresses의 각 요소에 speeds의 요소 더하는 걸 반복
- progresses의 0번 요소 값이 100 이상이 되면 pop(0) 하고 answer의 0번 요소에 1 추가 
- while문으로 작업 진도 0번 요소 값이 100 미만일 때까지 반복
- 없으면 answer의 1번 요소로 넘어가서 다시 추가 

### 사용한 함수 

### 코드 구현

<pre>
<code>

    def solution(progresses, speeds):
        #각 배포 마다 배포되는 기능 수 
        answer = []
        #answer의 각 배포 번호 관리 
        stack = 0
        
        
        while progressess:
            # 맨 앞 작업이 완료되지 않는 동안 
            while progresses[0] < 100: 
                # 각 작업에 개발 속도만큼 추가 반복 
                for i in range((0, len(progresses)):
                    progresses[i] + speeds[i]
            
            # 맨 앞 작업이 종료되면 작업과 속도를 리스트에서 빼버림 
            progresses.pop(0)
            speeds.pop(0)
            
            # answer의 stack 번호 요소에 1 추가 
            answer[stack] = answer[stack] + 1
            
            # pop 되고 나온 다음 순서 작업이 완료되어있지 않으면 배포 번호 다음으로 
            if progresses[0] < 100:
                stack = stack + 1
            
            # 완료되어있으면 작업 pop 되고 answer에 1 추가 
	return answer

</code>
</pre>


## 문제 출처
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42586)