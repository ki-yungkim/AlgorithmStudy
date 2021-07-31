# Algorithm_Step_8_다익스트라

## 8주차 1번  배달 문제 
***
  

### 문제 설명 
- N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을 수 찾기
- 마을의 개수 N 
- 각 마을을 연결하는 도로의 정보 road
- 음식 배달이 가능한 시간 K 
- 음식 주문을 받을 수 있는 마을의 개수 return
### 제한사항
- 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
- road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
- road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
- road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
- a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
- 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
- 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
- K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
- 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
- 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.

### 입출력 예시 
 | N    |road                                                     |K  |result|
 | :----|:--------------------------------------------------------|:--|:-----| 
 | 5    |[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]        |3  |4     |
 | 6    |[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]|4  |4     |


#### 예시 설명  
- 1번 노드는 2번, 4번 노드와 연결되며 각각 1, 2 시간이 걸린다 
- 2번 노드는 3번 노드와 연결되고 3시간이 걸린다
- 5번 노드는 2번 노드와 연결되고 2시간이 걸린다
- 5번 노드는 3번 노드와 연결되고 1시간이 걸린다
- 5번 노드는 4번 노드와 연결되고 2시간이 걸린다 
 
- K는 3이므로 3시간 이하로 배달 가능한 노드를 찾아야 한다
- 1 -> 2, 1 -> 4는 3시간 이하로 가능하다
- 1 -> 2 -> 5 는 3시간 이하로 가능하다 
- 배달 가능한 노드는 1, 2, 4, 5로 4개가 return 된다.

### 코드 구조 구상
- 다른 사람이 한 것을 따라서 해보았다
- 이해가 잘 안 가는 부분이 많아 공부 많이 해야할 것 같다
### 사용한 함수 
- 

### 코드 구현

-- 와샬-플로이드 방식 쓴 것을 참고하였다
<pre>
<code>
import math
def solution(N, road, K):
    answer = 0
    roads = [[math.inf for i in range(N)] for j in range(N)]
    print(roads)
    for r in road:
        if roads[r[1] - 1][r[0]-1] > r[2]:
            roads[r[1] - 1][r[0] -1] = r[2]
            roads[r[0] - 1][r[1] -1] = r[2]
    
    for i in range(N):
        roads[i][i] = 0

    for path in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][path] + roads[path][j]:
                    roads[i][j] = roads[i][path] + roads[path][j]

    for i in range(N):
        if roads[0][i] <= K:
            answer += 1
    return answer
</code>
</pre>

-- 다익스트라 알고리즘 코드 참고 
<pre>
<code>
import math
def solution(N, road, K):
    answer = 0
    visited = []
    distance = [0] + [math.inf for i in range(1, N)]
    roads = {i: {} for i in range(N)}
    for r in road:
        if r[1] - 1 in roads and r[0] - 1 in roads[r[1] - 1]:
            if roads[r[1] - 1][r[0] - 1] > r[2]:
                roads[r[1] - 1][r[0] - 1] = r[2]
                roads[r[0] - 1][r[1] - 1] = r[2]
        else:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in roads[0]:
        distance[i] = roads[0][i]

    while len(visited) != N:
        minimum = math.inf
        for i in range(1, N):
            if i not in visited and distance[i] < minimum:
                minimum = distance[i]
                town = i

        visited.append(town)
        for i in roads[town]:
            if distance[i] > distance[town] + roads[town][i]:
                distance[i] = distance[town] + roads[town][i]

    for d in distance:
        if d <= K:
            answer += 1

    return answer
</code>
</pre>
## 문제 출처 
[Programmers](https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3)


#참고 사이트 
https://dev-note-97.tistory.com/155