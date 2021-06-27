# Algorithm_Step_3_타겟 넘버

## 3주차 3번 타겟 넘버 문제 
***
  

### 문제 설명 
- 깊이 우선탐색(DFS)과 너비 우선탐색(BFS)
- n개의 음이 아닌 정수 
- 더하거나 빼서 타겟 넘버를 만든다 
- 사용할 수 있는 숫자가 담긴 배열 numbers
- 타겟 넘버 target
- 타겟 넘버를 만드는 방법의 수를 return 

### 제한사항
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

### 입출력 예시 
 | numbers          |target           |return           | 
 | :--------------- |:--------------- |:--------------- |
 | [1, 1, 1, 1, 1]  |3                |5                |
 

 

#### 예시 설명  
- -1+1+1+1+1 = 3
- +1-1+1+1+1 = 3
- +1+1-1+1+1 = 3
- +1+1+1-1+1 = 3
- +1+1+1+1-1 = 3

- 3을 만들 수 있는 경우의 수는 5가지 

### 코드 구조 구상
- 0부터 시작해서 +x, -x로 반복해서 나눠지는 그래프를 생각해본다
- 바닥까지 가야 값이 나오는 구조니까 깊이 우선 탐색(DFS)으로 한다

-       0
-   +x       -x
- +y -y    +y -y  
- ...

- numbers를 읽어서 각 요소들에 + - 한 것을 딕셔너리에 넣어서 연산 처리
- 연산한 값은 따로 변수를 만들어서 처리한다 


### 사용한 함수 
- 

### 코드 구현

### 내가 생각했던 방식 - 딕셔너리 key 중복 안되는 문제로 실패  
<pre>
<code>
def solution(numbers, target):
    graph = {}
    for i in range(len(numbers)-1):
        n = numbers[i]
        m = numbers[i+1]
        a = n
        b = -n
        c = m
        d = -m
        
        if a not in graph:
            graph[a] = [c, d]
        elif c not in graph[a]:
            graph[a].append(c)
        elif d not in graph[a]:
            graph[a].append(d)
        
        if c not in graph:
            graph[c]=[a]
        elif a not in graph[c]:
            graph[c].append[a]
        if d not in graph:
            graph[d]=[a]
        elif a not in graph[d]:
            graph[d].append(a0    
    
        
        if b not in graph:
            graph[b] = [c, d]
        elif c not in graph[b]:
            graph[b].append(c)
        elif d not in graph[b]:
            graph[b].append(d)
        
        if c not in graph:
            graph[c]=[b]
        elif a not in graph[c]:
            graph[c].append(b)
        if d not in graph:
            graph[d]=[b]
        elif a not in graph[d]:
            graph[d].append(b)  
    
    visited = []
    stack = [a]
    answer = 0
    
    while stack:
        x = stack.pop()
        if x not in visited:
            visited.append(x)
            if x in graph:
                tmp = list(set(graph[x]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
                
        if sum(visited) == target:
            answer += 1
         
    return answer


</code>
</pre>

### 다른 사람이 한 방식 참고 

#### 방식 1 : from itertools import product 사용 
product : 리스트의 모든 조합을 만들어준다 

<pre>
<code>
def solution(numbers, target):
    length = len(numbers)
    
    cases = []
    for _ in range(length):
        cases.append([-1, 1])
    cases = list(product(*cases))

    
    count = 0
    for case in cases:
        s = 0
        for i in range(length):
            s += case[i] * numbers[i]
        if s == target:
            count += 1
    return count
</pre>
</code>

#### 방식 2 : DFS 재귀함수 사용 

<pre>
<code>
answer = 0
def dfs(index, numbers, target, value):
    global answer 

    length = len(numbers)
    
    if(index == length and target == value):
        answer += 1
        return
    
    if(index == length):
        return 

    
    dfs(index+1, numbers, target, value + numbers[index])
    dfs(index+1, numbers, target, value - numbers[index])


def solution(numbers, target):
    global answer 
    dfs(0, numbers, target, 0)
    return answer 


</pre>
</code>


## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3)


#참고 사이트 

https://jellysong.tistory.com/68