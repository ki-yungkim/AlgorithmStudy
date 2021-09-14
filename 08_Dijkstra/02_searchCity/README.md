# Algorithm_Step_8_다익스트라

## 8주차 2번  특정 거리의 도시 찾기
***
  
### 문제 설명 
- 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
- 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
- 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
### 제한사항
- 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
- 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
- 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 
- 단, A와 B는 서로 다른 자연수이다.

### 입출력 예시 
- 입력 
    - 4 4 2 1
    - 1 2
    - 1 3
    - 2 3
    - 2 4

- 출력
    - 4
#### 예시 설명  
- 도시의 개수 N : 4
- 도로의 개수 M : 4
- 거리 정보 K : 2
- 출발 도시의 번호 X : 1

- 존재하는 도로 
- 1 -> 2
- 1 -> 3
- 2 -> 3
- 2 -> 4
 
- 1번 도시에서 출발하는데 거리가 2인 도시의 정보 

- 1과 바로 연결된 도로는 2와 3 
- 2, 3은 거리가 1이다
- 1에서 4로 가려면 1 -> 2 -> 4로 갈 수 있으며 거리가 2이다
- 그래서 출력되는 값은 4 1개
 

### 코드 구조 구상
- 너비우선 탐색

### 사용한 함수 
- 

### 코드 구현

<pre>
<code>
from collections import deque

n,m,k,x=map(int,input().split())
node=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    node[a].append(b)

dist=[-1]*(n+1)
dist[x]=0

q=deque([x])

while q:
    now=q.popleft()
    for i in node[now]:
        if dist[i] == -1:
            dist[i]=dist[now]+1
            q.append(i)

for idx,d in enumerate(dist):
    if d == k:
        print(idx)
        break
else:
    print(-1)
</code>
</pre>
## 문제 출처 
[백준](https://www.acmicpc.net/problem/18352)


#참고 사이트 
(https://zinirun.github.io/2020/09/18/ps-bfs-boj-18352/)