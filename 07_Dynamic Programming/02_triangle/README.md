# Algorithm_Step_7_동적계획법

## 7주차 2번 정수 삼각형 문제 
***
  

### 문제 설명 
- 삼각형 형태의 정보가 담긴 배열 triangle
- 아래 칸으로 이동할 때 대각선 왼쪽 또는 오른 쪽으로만 갈 수 있다.
- 거처간 숫자의 합의 최대값을 return 

### 제한사항
- 삼각형의 높이는 1 이상 500 이하입니다.
- 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

### 입출력 예시 
 | input                                                  | 
 | :------------------------------------------------------| 
 | [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]|
  

 | return    | 
 | :---------| 
 | 30        |

#### 예시 설명  
- 7 + 3 + 8 + 7 + 5 = 30 
 

### 코드 구조 구상
- 첫 값은 무조건 포함 -> triangle[0] 
- triangle의 길이 우선 체크 
- for문으로 규칙에 따라 합이 더해지게 해주고 max로 비교 

- 위에서부터 더해간다 
- i는 행, j는 열
- i는 1부터 N까지
- j는 i에 1 더한 값 까지
- [i-1][j]와 [i-1][j-1] 중에 큰 값을 더해간다 
- 양쪽 끝은 그 위의 끝 값을 가져온다 
- 마지막 행의 최대값을 출력한다 

### 사용한 함수 
- 

### 코드 구현

- 다른 사람과 거의 비슷하게 구상했다
- 다시 한번 풀어볼 필요가 있다
<pre>
<code>
def solution(triangle):
    N = len(triangle)       
    answer = 0
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])    
    answer = max(triangle[N-1])
    return answer    
</code>
</pre>

-

</code>
</pre>
## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3)


#참고 사이트 
https://codedrive.tistory.com/49