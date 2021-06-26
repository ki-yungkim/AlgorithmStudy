# Algorithm_Step_3_BFS_DFS

## 3주차 1번 DFS와 BFS 문제 
***
  

### 문제 설명 
- 깊이 우선탐색(DFS)과 너비 우선탐색(BFS)
- DFS -> 한 방향으로 쭉 
- BFS -> 시작에서 가까운 점 먼저 방문 

- 1번 줄 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V 
- 2번 줄부터 간선이 연결하는 두 정점의 번호 

- 출력 -> V 부터 방문한 점 순서대로  
- 1번 줄은 DFS를 수행한 결과
- 2번 줄은 BFS를 수행한 결과 
### 제한사항
- 1 ≤ N ≤ 1,000)
- 1 ≤ M ≤ 10,000
### 입출력 예시 
 | input     | 
 | :---------| 
 | 4 5 1     | 
 | 1 2       |
 | 1 3       | 
 | 1 4       |
 | 2 4       |
 | 3 4       |
 

 | return    | 
 | :---------| 
 | 1 2 4 3   |
 | 1 2 3 4   |
 

#### 예시 설명  
- 정점 1번부터 4번까지
- 간선 5개
- 1번 시작

- 1
- 2 3 
- 4 (1에서도 연결) 
- DFS 
    - 연결된 곳 끝까지 
    - 1에서 2로, 2와 연결된 4로, 4가 이 줄 마지막
    - 한 줄 끝냈으니 3으로 
    - 출력 -> 1 2 4 3

- BFS 
    - 옆으로 쭉 하고 아래 레벨로 
    - 1에서 2로, 2에서 3으로, 4로 
    - 출력 -> 1 2 3 4 
    
### 코드 구조 구상
- 

### 사용한 함수 
- map
- join
- sort 
- append
- pop()
- input 
- split 

### 코드 구현

<pre>
<code>

graph = {}
n = input().split(' ')
node, edge, start = map(int, n)
for i in range(edge):
    edge_number = input().split(' ')
    n1, n2 = map(int, edge_number)
    
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)


def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    return " ".join(map(str, visited))

def BFS(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return " ".join(map(str, visited))
  
print(DFS(graph, start))
print(BFS(graph, start))


</code>
</pre>


## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/1260)


#참고 사이트 
https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html