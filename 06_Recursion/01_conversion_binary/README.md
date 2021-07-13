# Algorithm_Step_6_재귀함수

## 6주차 1번 이진수 변환 문제 
***
  

### 문제 설명 
- 주어지는 1개의 자연수 N을 이진수로 바꿔서 출력 

   
### 제한사항
- 이진수는 0으로 시작하면 안 된다.

### 입출력 예시 
 | input     | 
 | :---------| 
 | 53        | 

 | return    | 
 | :---------| 
 | 110101    |

#### 예시 설명  
- 

### 코드 구조 구상
- bin() 쓰면 0b1111 이런 방식으로 나올 것이다
- 앞에 2개 빼고 출력시켜보자 


### 사용한 함수 
- 2진수로 변환해주는 bin()
- print(c[2:]) : c의 2번째부터 출력 

### 코드 구현
- 내가 푼 방식 

<pre>
<code>
import sys

a = sys.stdin.readline()
b = int(a)
c = bin(b)
print(c[2:])

</code>
</pre>

- 파이썬 이진수 변환 기능 안 쓰는 방식 
<pre>
<code>
import sys

def binary(n):
    if n > 1:
        binary(n//2)
        
    if n % 1 == 1:
        print(0, end = "")
    
    else:
        print(0, end = "")

n = sys.stdin.readline()
binary(int(n))

</code>
</pre>
## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/10829)


#참고 사이트 
[Baekjoon Online Judge](https://www.acmicpc.net/source/29437728)