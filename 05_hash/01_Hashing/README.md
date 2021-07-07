# Algorithm_Step_5_Hash

## 5주차 1번 Hashing 문제 
***
  

### 문제 설명 
- 영문 소문자 1부터 26까지 매칭 
- 첫 줄은 문자열의 길이 둘째 줄에 문자열 
- 입력 받은 영어 문자열의 해시 값은 영문소문자에 해당하는 번호와 문자열의 인덱스만큼 31의 제곱을 곱해준 값들의 합

   
### 제한사항
- 문자열은 모두 알파벳 소문자 


### 입출력 예시 
 | input     | 
 | :---------| 
 | 5         | 
 | abcde     |
 

 | return    | 
 | :---------| 
 | 4739715   |

#### 예시 설명  
- a : 1 * 31^0 
- b : 2 * 31^1 
- c : 3 * 31^2 
- d : 4 * 31^3 
- e : 5 * 31^4 

-> 위 계산 값들의 합 

### 코드 구조 구상
- 입력받는 배열 리스트로 
- 영문 소문자 1~26으로 해싱 
- 반복문 리스트 인덱스 번호 0부터 입력받은 문자열 길이만큼 
- 영소문자 리스트와 인덱스에 있는 값 비교해서 해싱한 값 추출
- 값 * 31^인덱스 
- result에 값 다 더하기 
- 큰 값들은 1234567891로 나눈 나머지로 계산

### 사용한 함수 
- 

### 코드 구현
- 

<pre>
<code>
import sys
from string import ascii_lowercase

n = sys.stdin.readline() 
x = sys.stdin.readline()
x_list = list(x)
alpha_list = list(ascii_lowercase)
hash = {}
for i in range(1, 27):
    hash[alpha_list[i-1]] = i

result_sum = 0
for i in range(len(x)):
     for j in range(26):
             if x_list[i]==alpha_list[j]:
                    result = hash[alpha_list[j]]
                    result_sum += result * 31 ** i
                    result_large = result_sum%1234567891 

print(result_large)


</code>
</pre>


## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/15829)


#참고 사이트 
