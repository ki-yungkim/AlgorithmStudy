# Algorithm_Step1_Stack_Queue
# 3번 다리를 건너는 트럭 
***

### 문제 설명 

- 1대의 트럭이 다리를 통과하는데 걸리는 시간은 bridge_length
- 한번에 올라갈 수 있는 트럭 수 bridge_length
- 다리가 버티는 한계 무게는 weigth
- 트럭의 무게는 truck_weigths [] 
- return은 트럭이 모두 통과하는데 걸리는 시간 

### 제한사항


### 입출력 예시 
 | bridge_length| weigth| truck_weigths                   | return|
 | :----------- | :-----| :-------------------------------| :-----|
 | 2            | 10    | [7, 4, 5, 6]                    | 8     |
 | 100          | 100   | [10]                            | 101   |
 | 100          | 100   | [10,10,10,10,10,10,10,10,10,10] | 110   |   

 

#### 설명  


### 코드 구조 구상



### 코드 구현

<pre>
<code>
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

</code>
</pre>
