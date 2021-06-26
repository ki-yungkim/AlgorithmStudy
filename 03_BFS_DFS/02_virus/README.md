# Algorithm_Step_3_바이러스

## 3주차 2번 바이러스 문제 
***
  

### 문제 설명 
- 깊이 우선탐색(DFS)과 너비 우선탐색(BFS)
- 네트워크 상에서 연결되어있는 컴퓨터들의 바이러스 전파 
- 연결 정보가 주어질 때 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력 

- 입력 첫째 줄은 컴퓨터의 수
- 컴퓨터의 수는 100 이하
- 컴퓨터는 1번부터 차례대로 번호 
- 둘째 줄은 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수 
- 세번째 줄부터 연결되어있는 컴퓨터 번호 쌍 정보 
### 제한사항
- 컴퓨터의 수는 100 이하 

### 입출력 예시 
 | input     | 
 | :---------| 
 | 7         | 
 | 6         |
 | 1 2       | 
 | 2 3       |
 | 1 5       |
 | 5 2       |
 | 5 6       |
 | 4 7       |
 

 | return    | 
 | :---------| 
 | 4         |
 

#### 예시 설명  
- 컴퓨터는 7대
- 연결 쌍은 6개
- 1 - 2 - 3 
- 1 - 5 - 6
- 5 - 2

- 4, 7은 연결이 없다
- 바이러스에 걸릴 수 있는 컴퓨터는 2, 3, 5, 6으로 4대

 
### 코드 구조 구상
- 너비우선탐색(BFS) 


### 사용한 함수 
- int 
- input
- append 
- pop 


### 코드 구현

<pre>
<code>

graph = {}
computer = int(input())
edge = int(input())

for i in range(edge):
    edge_number = input().split(' ')
    c1, c2 = map(int, edge_number)
    
    if c1 not in graph:
        graph[c1] = [c2]
    elif c2 not in graph[c1]:
        graph[c1].append(c2)

    if c2 not in graph:
        graph[c2] = [c1]
    elif c1 not in graph[c2]:
        graph[c2].append(c1)


def BFS(graph):
    visited = []
    queue = [1]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return len(visited)
  
print(BFS(graph)-1)


</code>
</pre>


## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/2606)


#참고 사이트 