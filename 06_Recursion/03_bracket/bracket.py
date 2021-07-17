def check(u):
    # u가 올바른 괄호 문자열인지 확인 
    # () -> stack = []
    # )( -> error
    stack = []
    try:
        for i in u:
            if i == '(':
                stack.append('1')
            else:
                stack.pop()
        return True
    except:
        return False

def divide(p):
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u = ''
    v = ''
    for i in range(len(p)):
        u += p[i]
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
        if u.count('(') == u.count(')'):
            # v는 빈 문자열이 될 수 있습니다. 
            v = p[i+1:]
            break
    return u, v

    
def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    answer = ''
     # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    while p:
        # u, v로 나눈 문자열 
        u, p = divide(p)
        # u가 올바른 괄호 문자열이면 
        if check(u):
            # 빈 문자열인 answer에 u 추가  
            # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
            answer += u
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면     
        else:
            # 문자열의 방향 뒤집기 
            temp = ''
            for i in u:
                if i == '(':
                    temp += ')'
                else:
                    temp += '('
            reverse = temp[1:-1]       
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            # 4-3. ')'를 다시 붙입니다. 
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 뒤집은 문자열 붙이기   
            answer += '(' + solution(p) + ')' + reverse
            break
    # 4-5. 생성된 문자열을 반환합니다.        
    return answer