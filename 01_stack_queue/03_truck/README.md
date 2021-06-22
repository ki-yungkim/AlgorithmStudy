# Algorithm_Step1_Stack_Queue
## 3번 다리를 건너는 트럭 
***

### 문제 설명 
- 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 반환
- 1대의 트럭이 다리를 통과하는데 걸리는 시간은 bridge_length
- 한번에 올라갈 수 있는 최대 트럭 수 bridge_length
- 다리가 버티는 한계 무게는 weigth
- 트럭의 무게는 truck_weigths []  

### 제한사항
- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

### 입출력 예시 
 | bridge_length| weigth| truck_weigths                   | return|
 | :----------- | :-----| :-------------------------------| :-----|
 | 2            | 10    | [7, 4, 5, 6]                    | 8     |
 | 100          | 100   | [10]                            | 101   |
 | 100          | 100   | [10,10,10,10,10,10,10,10,10,10] | 110   |   

#### 설명  
- 무게 7인 트럭이 올라가있으면 그 다음 무게 4인 트럭은 못 올라감 
- 2초가 지나 1번 트럭이 통과하면 3초부터 무게 4인 트럭이 올라갈 수 있음 
- 무게 4 + 5 < 10 이므로 4초에는 무게 5인 트럭이 올라갈 수 있음 
- 5초에는 5 + 6 > 10 이므로 4번 트럭이 올라갈 수 없음
- 6초에는 3번 트럭은 지나갔고 4번 트럭이 올라감
- 7초에 다리를 통과하고 8초에 완료 

### 코드 구조 구상
- answer는 0초로 시작
- 다리 길이만큼 [0]이 있는 리스트 
- 시작하면 answer에 1초 추가
- position에서 맨 앞 요소 pop 

- truck_weights가 남아있고 
- (지금 들어오는 트럭 무게 + 다리 위에 있는 무게) <= weight인지 확인 
- 가벼우면 truck_weights의 첫 요소를 position 맨 뒤에 추가
- 아니면 position 맨 뒤에 0 추가 
- 1초 추가하고 
- position에서 맨 앞 요소 pop
- 지금 트럭 + 다음 트럭 무게가 무게 제한보다 가벼우면 트럭 무게를 position에 추가   
- 아니면 position 맨 뒤에 0 추가

- 첫 예시일 때

| position     | truck_weigths | answer|
| :----------- |  :------------| :-----|
| [0, 0]       | [7, 4, 5, 6]  | 0     |
| [0, 7]       | [4, 5, 6]     | 1     |
| [7, 0]       | [4, 5, 6]     | 2     |
| [0, 4]       | [5, 6]        | 3     |
| [4, 5]       | [6]           | 4     |
| [5, 0]       | [6]           | 5     |
| [0, 6]       | []            | 6     |
| [6, 0]       | []            | 7     |
| [0]          | []            | 8     |

### 사용한 함수 

### 코드 구현

<pre>
<code>
    def solution(bridge_length, weight, truck_weights):
        # 걸린 시간 
        answer = 0
        # 다리 위의 트럭 위치와 무게 
        position = [0] * bridge_length
        
        # 트럭이 다리 위에 있는 동안
        while position:
            answer += 1          
            # 앞에 있는 트럭이나 0 빼주기 
            position.pop(0)
            
            # 대기하는 트럭이 있으면 
            if truck_weights:
                # 다음 순서 트럭과 다리 위의 트럭 무게가 무게 제한 이하면 
                if truck_weights[0] + sum(position) <= weight:
                    # position에 다음 순서 트럭 추가 
                    position.append(truck_weights.pop(0))
                else:
                    # 아니면 0 추가 
                    position.append(0)
        
    
    return answer

</code>
</pre>

## 문제출처
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42583)