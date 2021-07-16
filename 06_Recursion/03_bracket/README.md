# Algorithm_Step_6_재귀함수

## 6주차 3번 괄호변환 문제 
***
  

### 문제 설명 
- '(' 와 ')'의 수가 같은 문자열 p
- 올바르게 된 문자열을 return한다. 
- 입력이 빈 문자열일 경우 빈 문자열 반환 

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

### 입출력 예시 
 | input     | 
 | :---------| 
 | "(()())()"| 

 | return    | 
 | :---------| 
 | "(()())()"|

 | input     | 
 | :---------| 
 | ")("      | 

 | return    | 
 | :---------| 
 | "()"      |
#### 예시 설명  
- 

### 코드 구조 구상
- 

### 사용한 함수 
- 

### 코드 구현
- 다른 사람의 풀이 
<pre>
<code>
def check(u):
    stack = []
    try:
        for i in u:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
        return True
    except:
        return False

def divide(p):
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    n = ''
    v = ''
    for i in range(len(p)):
        n += p[i]
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
        if n.count('(') == n.count(')'):
            # v는 빈 문자열이 될 수 있습니다. 
            v = p[i+1:]
            break
    return n, v

    
def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    answer = ''
    while p:
        u, p = divide(p)
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. while
        if check(u):
            # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
            answer += u
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.    
        else:
            temp = ''
            for i in u:
                if i == '(':
                    temp += ')'
                else:
                    temp += '('
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            # 4-3. ')'를 다시 붙입니다. 
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.         
            answer += ('(' + solution(p) + ')' + temp[1:-1])
            break
    # 4-5. 생성된 문자열을 반환합니다.        
    return answer
</code>
</pre>

- 다른 사람의 풀이 
<pre>
<code>
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
</code>
</pre>
## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3)


#참고 사이트 
https://ysyblog.tistory.com/91