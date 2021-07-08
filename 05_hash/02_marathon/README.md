# Algorithm_Step_5_Hash

## 5주차 2번 완주하지 못한 선수 문제 
***
  

### 문제 설명 
- 마라톤 참가자 이름 배열 participant  
- 완주한 선수 이름 배열 completion
- 완주하지 못한 선수 이름을 return 


### 제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.


### 입출력 예시 
 | participant                                      |  completion                             | return     |
 | :------------------------------------------------| :--------------------------------       | :--------- |
 | ["leo", "kiki", "eden"]                          | ["eden", "kiki"]                 | "leo"      |
 | ["marina", "josipa", "nikola", "vinko", "filipa"]| ["josipa", "filipa", "marina", "nikola"]| "vinko"    |
 | ["mislav", "stanko", "mislav", "ana"]            | ["stanko", "ana", "mislav"]             | "mislav"   |
 

#### 예시 설명  
- 첫번째 : 중복되지 않는 인원 leo return
- 두번째 : 중복되지 않는 인원 vinko return 
- 세번째 : mislav가 두명인데 completion에 한명 뿐이므로 mislav return 


### 코드 구조 구상
- 배열 비교 
- 배열 - 배열로 중복되는 값 제거
- 동명 이인 체크 방법  구상 필요 
- 정렬 시키고 hash로 매칭, 남는 것 출력 
### 사용한 함수 
- 

### 코드 구현
- Try 1
- 동명이인 처리는 안되는데 일단 중복 제거 시도 

<pre>
<code>
def solution(participant, completion):
    
    answer = list(set(participant) - set(completion))
    if answer:
        return answer[0]

</code>
</pre>

- Try 2
- hash의 pop을 이용해서 같은 이름을 pop 해보았다.
- 런 타임 에러도 많이 나고 역시 동명이인 해결이 안된다
<pre>
<code>
def solution(participant, completion):
    
    hash = {}
    for i in range(len(participant)):
        hash[participant[i]] = i
    
    for i in range(len(completion)):
        hash.pop(completion[i])
    
    for k in hash.keys():
        return k
        

</code>
</pre>

- Try 3
- 참가자 정렬해주고 중복되는 값 뽑아서 맨 뒤로 보내는 방식
- 테스트는 다 통과
- 동명이인도 처리 가능 
- 시간 초과 문제 발생 
 
<pre>
<code>
def solution(participant, completion):
    participant.sort()
    completion.sort()
    x = 0
    for i in range(len(participant)-1):
        if participant[i] == participant[i+1]:
            x = participant.pop(i)
            participant.append(x) 
    
    
    while completion:
        i = 0;
        if participant[i] == completion[i]:
            participant.pop(0)
            completion.pop(0)
    return participant[0]
        

</code>
</pre>


- 다른 사람 풀이 참고
- 이름을 key, 인원 수를 value 

<pre>
<code>
def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in completion:
        if hash[i]==1:
            del hash[i]    
        else:
            hash[i]-=1
    return list(hash.keys())[0]
        

</code>
</pre>

- 다른 사람 풀이 참고
- counter 
- 몇개씩 있는지 계산 해준다.

<pre>
<code>
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]
        

</code>
</pre>
## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3)


#참고 사이트 
https://velog.io/@huga/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%B4%EC%8B%9C-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98