# Algorithm_Step_2_bruteForce_binarySearch

## 2주차 3번 숫자카드 2 문제 
***
  

### 문제 설명 
- 정수 하나가 적혀있는 숫자카드
- 정수 M개가 주어졌을 때 같은 숫자 카드를 몇개 가지고 있는지 
- 1번 줄 : 숫자 카드의 수
- 2번 줄 : 가지고 있는 숫자 카드 값들
- 3번 줄 : 숫자 카드 수
- 4번 줄 : 몇개인지 구할 숫자들 

- 4번 줄에 있는 숫자들이 2번 줄에 있는 숫자들 중에 몇개가 있는지 출력한다.

### 제한사항
- 숫자 카드의 개수는 1 ≤ N ≤ 500,000
- 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

### 입출력 예시 
 | input                     | 
 | :-------------------------| 
 | 10                        | 
 | 6 3 2 10 10 10 -10 -10 7 3|
 | 8                         | 
 | 10 9 -5 2 3 4 5 -10       |

 | return                    | 
 | :-------------------------| 
 | 3 0 0 1 2 0 0 2           |
 

#### 예시 설명  
- 4번 줄의 10은 2번 줄에 3개
- 4번 줄의 9는 2번 줄에 0개
- 4번 줄의 -5 는 2번 줄에 0개
- 4번 줄의 2는 2번 줄에 1개
    .
    .
    .
- 4번 줄의 -10은 2번 줄에 2개 


### 코드 구조 구상
- 입력해주는 함수 필요
- 입력되는 숫자들 분리해서 저장
- 숫자 개수 카운팅 기능
- f-string으로 문자열 포매팅

### 사용한 함수 
- stdin.readline() 
    - 입력 받는 메서드 
    - input() 보다 빠르다 
 
- Counter
    - 문자를 하나 하나 나눠서 몇개 있는지 체크 해준다
 
- f'{ }'
    - f-string : 문자열로 포매팅 
 
- print(x, end = ' ')
 - print는 기본 값이 줄바꿈이다.
 - 줄바꿈 대신 공백이 들어가게 처리 

### 코드 구현

<pre>
<code>

from sys import stdin
from collections import Counter

# 각각 값을 입력받고 숫자 카드들은 split 해서 나누어둔다
a = stdin.readline()
b = stdin.readline().split()
c = stdin.readline()
d = stdin.readline().split()

# b에 숫자들이 각각 몇개인지 카운트 해서 딕셔너리로 저장
C = Counter(b)

# d에 있는 값 i가 C에 있으면 출력하고 공백 아니면 0 출력하고 공백 
# 딕셔너리라서 [i] 하면 해당 갯수가 나온다  
for i in d:
    if i in C:
        print(f'{C[i]}', end=' ')
    else: 
        print('0', end=' ')
</code>
</pre>


## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/10816)