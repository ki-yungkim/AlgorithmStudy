# Algorithm_Step_4_Base Conversion_Bitwise Operation

## 4주차 1번 팩토리얼 진법 문제 
***
  

### 문제 설명 
- 팩토리얼 진법 
- i번 자리의 값은 a_i * i! 
- 팩토리얼 진법의 719는 10진법의 53
    - 7 * 3! + 1 * 2! + 9 * 1! 
    - (7 * 3*2*1) + (1 * 2*1) + (9 * 1)
    - 42 + 2 + 9 = 53
- 팩토리얼 진법으로 작성된 숫자가 주어졌을 때, 10진법으로 읽은 값을 구하는 프로그램 
- 입력은 여러개의 테스트 케이스 
- 각 테스트 케이스는 한 줄 
- 입력의 마지막 줄에는 0이 하나    
   
### 제한사항
- 팩토리얼 진법의 길이는 최대 5자리 

### 입출력 예시 
 | input     | 
 | :---------| 
 | 719       | 
 | 1         |
 | 15        | 
 | 110       |
 | 102       |
 | 0         |
 

 | return    | 
 | :---------| 
 | 53        |
 | 1         |
 | 7         |
 | 8         |
 | 8         |

#### 예시 설명  
- 1 : 1 * 1! 
- 15 : 1 * 2! + 5 * 1! = 7
- 110 : 1 * 3! + 1 * 2! + 0 * 1! = 8
- 102 : 1 * 3! + 0 * 2! + 2 * 1! = 8
    
### 코드 구조 구상
- 입력된 팩토리얼 숫자의 자릿수 길이 저장
- 입력된 팩토리얼 진법 숫자를 자리수 별로 나누기
- 팩토리얼 함수 쓰는 방식과 반복문으로 구현하는 방식 둘 다 구현해보기 
- while 문 
- length에 -1씩 하면서 
- a * math.factorial(length)


### 사용한 함수 
- 

### 코드 구현

<pre>
<code>

import math 
import sys
while True:
    try:
        digit=[]
        n = sys.stdin.readline().rstrip()
      
        digit = list(map(int, list(n)))
        length = len(digit)
       
        r = 0
        result = 0
        while digit:
            result +=  math.factorial(length) * digit.pop(0)             
            length -= 1
        if result != 0:
            print(result)
        
    except:
        break

</code>
</pre>


## 문제 출처 
[Baekjoon Online Judge](https://www.acmicpc.net/problem/5692)


#참고 사이트 