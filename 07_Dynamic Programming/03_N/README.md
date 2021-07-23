# Algorithm_Step_7_N으로 표현

## 7주차 3번 N으로 표현 문제 
***
  

### 문제 설명 
- 숫자 N과 number를 입력받는다 
- N을 가지고 사직연산만 가지고 number 값을 표현한다.
- N과 사칙연산만 사용해서 표현할 수 있는 방법 중 N 사용횟수의 최솟값을 return
- 12 = 5 + 5 + (5 / 5) + (5 / 5) -> 5를 6번 사용 
- 12 = 55 / 5 + 5 / 5 -> 5를 5번 사용 
- 12 = (55 + 5) / 5 -> 5를 4번 사용
- return = 4
### 제한사항
- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

### 입출력 예시 
 | input |
 | :---- |
 |  5    |
 | number|
 | :---- |
 |  12   |
 | return|
 | :---- |
 |  4    |
  
 | input |
 | :---- |
 |  2    |
 | number|
 | :---- |
 |  11   |
 | return|
 | :---- |
 |  3    |

#### 예시 설명  
- 2/11/3
- 11 = 22/2 -> 3번
 

### 코드 구조 구상
- 

### 사용한 함수 
- 

### 코드 구현

- 이해가 안가서 다른 사람 풀이 참조
<pre>
<code>
def solution(N, number):
	
    dp  =[set([N*int('1'*i)]) for i in range(1, 9)] 
    
    for i in range(8): 
        for j in range(i):
            for num1 in dp[j]:  
                for num2 in dp[i-j-1]: 
                	
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1//num2) 
                        
        if number in dp[i]:
            return i+1 
    return -1
</code>
</pre>

-

</code>
</pre>
## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3)


#참고 사이트 
https://cocook.tistory.com/113