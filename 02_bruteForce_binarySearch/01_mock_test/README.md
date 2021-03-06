# Algorithm_Step_2_bruteForce_binarySearch

## 2주차 1번 모의고사 문제 
***

### 문제 설명 
- 문제를 찍는 세명의 사람  
- 1번은 [1,2,3,4,5]를 반복한다 
- 2번은 [2,1,2,3,2,4,2,5]를 반복한다
- 3번은 [3,3,1,1,2,2,4,4,5,5]를 반복한다

- 1번부터 마지막 문제까지의 정답이 들어간 배열 -> answer
- 가장 많이 맞춘 사람이 누구인지 -> return 

### 제한사항
- 시험은 최대 10,000문제
- 문제의 정답은 1, 2, 3, 4, 5 중 하나
- 가장 높은 점수를 받은 사람이 여럿일 경우 return 오름차순 정렬 

### 입출력 예시 
 | answer          | return          |
 | :-------------- | :-------------- |
 | [1, 2, 3, 4, 5] | [1]             |
 | [1, 3, 2, 4, 2] | [1, 2, 3]       |
 

#### 설명  
- [1, 2, 3, 4, 5] 순서일 때
    - 1번은 5개 모두 맞추고 2번, 3번은 0개를 맞춘다. 
    - 가장 높은 점수는 1번
- [1, 3, 2, 4, 2] 순서일 때
    - 1번은 2개, 2번은 2개, 3번은 2개를 맞춘다. 
    - 1, 2, 3번 모두 동점

### 코드 구조 구상

- 정답 배열의 크기에 따라 얼마나 반복할 지 결정된다.
- python에서 나머지를 출력해주는 % 사용  
- % 써서 나온 나머지가 반복되는 배열의 요소 위치 
- 각 반복되는 배열의 요소와 정답의 요소가 맞으면 점수에 1씩 추가
- 동점인 경우를 감안하여 max 값이 여러개인 경우 다 append 해주는 방식으로 한다.

### 사용한 함수 
- i in range 
- python %
- len()
- max()
- .append 

### 코드 구현

<pre>
<code>

    def solution(answers):
    
    answer = []
    score = [0, 0, 0]
    a = [1,2,3,4,5] 
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            score[0] += 1
        if b[i%len(b)] == answers[i]:
            score[1] += 1
        if c[i%len(c)] == answers[i]:
            score[2] += 1
    
    for i in range(0, len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer

</code>
</pre>

## 문제출처
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42840)