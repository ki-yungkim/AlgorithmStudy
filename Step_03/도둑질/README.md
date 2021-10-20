# Algorithm
# 3단계
## 1주차 2번 도둑질 
***
  

### 문제 설명 
- 원형으로 연결되어 있는 집들  
- 서로 인접한 집은 털 수 없다 
- 첫 집과 마지막 집은 연결되어있다 
- 각 집에 있는 돈 배열이 주어진다. 
- 털 수 있는 최대 금액을 출력

### 제한사항
- 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
- money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

### 입출력 예시 
 | money       |return|
 |:------------|:-----|
 |[1, 2, 3, 1] |4     |


#### 예시 설명  
- 

### 코드 구조 구상
- 동적 계획법
### 사용한 함수 


### 코드 구현

<pre>
<code>
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
</code>
</pre>


## 문제 출처 
[Programmers](https://programmers.co.kr/learn/courses/30/lessons/42897)


#참고 사이트 
