# Algorithm_Step_4_Base Conversion_Bitwise Operation

## 4주차 2번 진법변환 문제 
***
  

### 문제 설명 
- B진법의 수 N 
- N을 10진법으로 바꿔서 출력하는 프로그램 
- 첫째 줄에 N과 B (2 <= B <= 36)
- A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
   
### 제한사항
- B 진법 수 N을 10진법으로 바꾸면 항상 10억보다 작거나 같다.

### 입출력 예시 
 | input     | 
 | :---------| 
 | ZZZZZ 36  | 


 | return    | 
 | :---------| 
 | 60466175  |

#### 예시 설명  
- Z = 35
- 36진법 
    
### 코드 구조 구상
- N진법의 숫자를 10진법으로 바꾸는 방법
- 2진법 1111 -> 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0
- 각 자리수에 N의 제곱을 하나씩 추가해가면서 곱해주면 된다
- 입력되는 값 중에 문자도 있으므로 String으로 받아야 한다
   

### 사용한 함수 
- input 

### 코드 구현
- 파이썬 input 기능 사용  
<pre>
<code>
number, base = input().split(" ")
base = int(base)
print(int(number,base))

</code>
</pre>

- 반복문으로 구현 
<pre>
<code>
from string import ascii_uppercase 

number, base = input().split(" ")
base = int(base)

digit = []
digit = list(number)

alphabet_list = list(ascii_uppercase)
numbers_list = list(range(10,36))

length = len(digit)
result = 0
nSquare = length - 1 
for i in range(length):
    index = 0
    if digit[i].isdigit():
        result += int(digit[i]) *  (base ** nSquare)
    else:
        index = alphabet_list.index(digit[i])
        result += numbers_list[index] *  (base ** nSquare)
    nSquare -= 1  

print(result)
   
</code>
</pre>







## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/2745)


#참고 사이트 
