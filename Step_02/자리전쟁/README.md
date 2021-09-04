# Algorithm
# 2단계
## 1주차 2번 자리전쟁
***
R x C의 형태를 지닌 전차 안에는 의자와 사람들의 정보들이 주어진다. 사람들은 다리가 아픈 것을 매우 싫어하기 때문에 빈 의자가 보이면 무조건 앉으려고 한다.

하지만 나보다 의자에 가까이 있는 사람이 보이면, 그 사람이 먼저 앉는다는 것을 알기 때문에 양보할 수밖에 없다.

만약, 나보다 의자에 가까이 있는 사람은 없지만, 같은 거리에 있는 사람이 있으면 서로 자리를 차지하려고 할 것이므로, 그 자리는 전쟁터가 될 것이다. (심지어 모든 사람들은 싸움에 자신있기 때문에, 이러한 전쟁터를 거부하지 않는다(!) )
여러분들은 이 전차의 정보가 주어질 때, 전쟁터가 될 자리의 수를 세어주면 된다.

A행 B열에서 C행 D열과의 떨어진 거리 Dist는 다음과 같은 유클리드 거리로 계산된다.

Dist² = (A-C)² + (B-D)²  


첫 줄에는 R과 C가 입력된다. (1 ≤ R ≤ 100) and (1 ≤ C ≤ 100)

이후 R개의 줄에 걸쳐 문자가 C개씩 주어진다. 이 문자는 '.' (빈 공간), 'X' (사람), 'L' (좌석) 만 주어지는 것이 보장된다.

'X'와 'L' 문자는 적어도 하나 이상이 주어짐이 보장되고, 하나의 'X' 문자와 같은 거리에 떨어진 'L'은 2개 이상 존재하지 않음이 보장된다.

### 문제 설명 
- 
### 제한사항
- 

### 입출력 예시 
- 입력
    - 4 4
    - .LX.
    - .X..
    - ....
    - .L..

- 출력
    - 1

#### 예시 설명  
- 

### 코드 구조 구상

### 사용한 함수 
- 

### 코드 구현


<pre>
<code>
    n,m = map(int,input().split())
    graph = []
    w_location = []
    b_location = []
    for i in range(m):
        graph.append(list(map(str,input())))
        for j in range(n):
            if graph[i][j]=='W':
                w_location.append([i,j])
            else:
                b_location.append([i,j])
                
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
     
    def dfs(x,y,color):
        global cnt
        cnt+=1
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n and graph[xx][yy]==color and visited[xx][yy]==0:
                visited[xx][yy] = visited[x][y]+1
                dfs(xx,yy,color)
               
    # W 체크
    visited = [[0]*n for _ in range(m)]
    cnt_w = 0
    for x,y in w_location:
        cnt = 0
        if visited[x][y]==0:
            visited[x][y] = 1
            dfs(x,y,'W')
        cnt_w += cnt*cnt
    print(cnt_w,end=' ')
     
    # B 체크
    visited = [[0]*n for _ in range(m)]
    cnt_b = 0
    for x,y in b_location:
        cnt = 0
        if visited[x][y]==0:
            visited[x][y] = 1
            dfs(x,y,'B')
        cnt_b += cnt*cnt
    print(cnt_b,end=' ')
</code>
</pre>


## 문제 출처 
[백준](https://www.acmicpc.net/problem/2886)


#참고 사이트 
(https://jiwon-coding.tistory.com/114)

