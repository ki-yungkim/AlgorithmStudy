# Algorithm_Step_5_Hash

## 5주차 3번 전화번호 목록 문제 
***
  

### 문제 설명 
- 번호를 담은 배열 phone_book
- 어떤 번호가 다른 번호의 접두어인 경우 false 출력 아니면 true 출력 

### 제한사항
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.
- 같은 전화번호가 중복해서 들어있지 않습니다.


### 입출력 예시 
 | phone_book                         |return      |
 | :----------------------------------| :--------- |
 | ["119", "97674223", "1195524421"]  | false      |
 | ["123","456","789"]                | true       |
 | ["12","123","1235","567","88"]     | false      |
 

#### 예시 설명  
- 1번 -> 119가 세번째 요소의 접두어 -> false
- 3번 -> 12가 두번쨰, 세번째 요소의 접두어 -> false 


### 코드 구조 구상
- 정렬시키면 같은 식으로 시작하는 것들이 모인다 
- 0번 요소가 1번 요소에 들어있는지 체크 
### 사용한 함수 
- 

### 코드 구현
- Try 1
- 기본 테스트는 통과하는데 제출하면 틀린 것들이 나온다
- 접두사가 되는게 맨 앞에 오는게 아닌 것이 있는거 같다.

<pre>
<code>
def solution(phone_book):
    
    phone_book.sort()
   
    a = phone_book[0]
    b = phone_book[1]
    
    if a in b:
        answer = False
    else:
        answer = True
    return answer

</code>
</pre>

- Try 2
- 테스트 13번 빼고 정확성, 효율성 테스트 모두 통과했다
- 접두사가 아니라 중간에 겹치는 것까지 false로 나오는 것 같다 

<pre>
<code>
def solution(phone_book):
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1] 
        if a in b:
            return False         
    return True

</code>
</pre>

- Try 3
- 앞에서부터 슬라이싱 해서 중간 문자도 false로 나오지 않게 처리했다
<pre>
<code>
def solution(phone_book):
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1][:len(a)] 
        if a in b:
            return False         
    return True

</code>
</pre>


## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3)


#참고 사이트 
https://blockdmask.tistory.com/425