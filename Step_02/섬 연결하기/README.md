# Algorithm
# 2단계
## 1주차 1번 섬 연결하기 
***
  

### 문제 설명 
- n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
- 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
### 제한사항
- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 ((n-1) * n) / 2이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

### 입출력 예시 
 | n    |costs                                     |return|
 | :----|:-----------------------------------------|:-----|
 | 4    |[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] |4     |


#### 예시 설명  
- 

### 코드 구조 구상
- 탐욕법
- 비용을 기준으로 오름차순 정렬
- set을 활용 출발, 도착 처음 지점 저장
- for 문으로 출발, 도착 지점이 둘 다 있으면 무시
- 하나만 있으면 
- set에 출발, 도착 지점을 추가 (중복 제거)
- answer에 비용을 추가
- costs 원래 리스트 값을 -1로
### 사용한 함수 
- 람다표현식
- enumerate : 인덱스 값을 포함한 값을 반환 

### 코드 구현
- 어려워서 다른 사람이 한 코드를 보고 작성해보았다.
- 다시 해볼 예정

<pre>
<code>
def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    routes = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while n != len(routes):
        for i, v in enumerate(costs[1:]):
            if v[0] in routes and v[1] in routes:
                continue
                
            if v[0] in routes or v[1] in routes:
                routes.update([v[0], v[1]])
                answer += v[2]
                costs[i+1] = [-1, -1, -1]
                break
    return answer
</code>
</pre>


## 문제 출처 
[Programmers](https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3)


#참고 사이트 
https://bladejun.tistory.com/93
