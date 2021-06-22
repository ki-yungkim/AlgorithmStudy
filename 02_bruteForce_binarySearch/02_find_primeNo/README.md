# Algorithm_Step_2_bruteForce_binarySearch

## 2주차 2번 소수찾기 문제 
***
- 이분 탐색으로 찾아야 하는 것 같은데 해결이 안되서 다른 방법 찾아서 처리
- 다른 사람들이 풀어놓은 것 보고 공부 중  

### 문제 설명 
- 임의의 숫자가 (numbers) 주어지고 그 숫자를 하나씩 요소로 하여 조합
- 조합해서 만들어지는 수 중에 소수가 몇개인지 return 


### 제한사항
- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

### 입출력 예시 
 | answer          | return          |
 | :-------------- | :-------------- |
 | "17"            | 3               |
 | "011"           | 2               |
 

#### 설명  
- 1과 7로 만들 수 있는 소수
 - 7, 11, 17
 - 3개
 
- 0, 1, 1로 만들 수 있는 소수
 - 11, 101
 - 2개 

### 코드 구조 구상

- 에라토스테네스의 체 
 - 2는 소수이므로 2를 쓰고 2의 배수를 지움 -> 3은 소수이므로 3을 쓰고 3의 배수를 지움 
 - 5는 소수이므로 5를 쓰고 5의 배수를 지움 -> ...
 - 소수의 제곱보다 작은 범위의 배수들만 지워도 충분
  - 100까지면 11의 제곱인 121보다 작으므로 7의 배수까지 지운다. 

- python의 permutations 사용 
- 요소들로 만들 수 있는 순열을 다 만들어준다.
- 1개로 만들어진 것 부터 numbers의 길이만큼으로 만들어진 것까지 만든다. 
- 집합에 순열들을 다 넣어준다.
- 0과 1은 소수가 아니므로 뺀다.
- 집합에서 2부터 시작해서 배수들을 빼준다. 
- 최고 값의 제곱근 이하까지 진행 
- 남은 수 갯수 반환 

### 사용한 함수 
- i in range 
- len(문자열)
- permutations(문자열, 요소 몇개로 만들지)
- map(함수, 값) : 함수를 값에 적용
- set : 집합 
- |= : 합집합
- max() 

### 코드 구현

<pre>
<code>

    from itertools import permutations

        def solution(numbers):
        answer = set()
        
        for i in range(len(numbers)):
            answer |= set(map(int, map(''.join, permutations(numbers, i+1))))
        
        answer -= set(range(2))
        
        for i in range(2, int(max(answer)**0.5) + 1):
            answer -= set(range(i*2, max(answer) + 1 , i))    
    
    return len(answer)
  

</code>
</pre>


## 문제 출처 
[프로그래머스 ](https://programmers.co.kr/learn/courses/30/lessons/42839)