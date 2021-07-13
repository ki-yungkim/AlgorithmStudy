# Algorithm_Step_6_재귀함수

## 6주차 2번 팩토리얼 문제 
***
  

### 문제 설명 
- 주어지는 1개의 자연수 N의 팩토리얼을 출력

   
### 제한사항
- 정수 N(0 ≤ N ≤ 12)

### 입출력 예시 
 | input     | 
 | :---------| 
 | 10        | 

 | return    | 
 | :---------| 
 | 3628800   |

 | input     | 
 | :---------| 
 | 0         | 

 | return    | 
 | :---------| 
 | 1         |
#### 예시 설명  
- 

### 코드 구조 구상
- 팩토리얼 함수 
- 재귀함수로 1부터 곱해가는 함수 

### 사용한 함수 
- 

### 코드 구현
- 팩토리얼 함수 사용  

<pre>
<code>
import math
import sys

a = sys.stdin.readline()
print(math.factorial(int(a)))

</code>
</pre>

- 재귀함수 사용 
<pre>
<code>
import sys

def factorial(n):

  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return n * factorial(n-1)
    
n = sys.stdin.readline()
print(factoral(int(n)))

</code>
</pre>
## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/10872)


#참고 사이트 
