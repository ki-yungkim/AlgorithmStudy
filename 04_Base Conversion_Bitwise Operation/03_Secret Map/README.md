# Algorithm_Step_4_Base Conversion_Bitwise Operation

## 4주차 3번 비밀지도 문제 
***
- 비트연산

### 문제 설명 
- 지도는 한변의 길이가 n인 정사각형 배열 형태
- 각 칸은 공백(" ") 또는 벽("#") 두 종류
- 전체 지도는 두장 지도 겹쳐서 얻을 수 있다.
- 지도 1, 2 중 하나라도 벽이면 전체 지도에서 벽
- 지도 1, 2 중 모두 공백이면 전체 지도에서 공백 
- 지도 1, 2는 정수 배열로 암호화 
- 각 가로줄에서 벽을 1, 공백을 0 으로 해서 얻어지는 이진수 값 

- 입력 형식 
    - 지도의 한변의 크기 n, 2개의 정수 배열 arr1, arr2 
    - 정수 배열의 각 원소 x를 이진수로 변환했을 때 길이는 n 이하 

- 출력형식 
    - '#', ' '으로 구성된 문자열 배열로 출력  

### 제한사항
- 

### 입출력 예시 
 | input      | value                             | 
 | :----------| :---------------------------------| 
 | n          | 5                                 | 
 | arr1       | [9, 20, 28, 18, 11]               | 
 | arr2       | [30, 1, 21, 17, 28]               | 


 | return                                         |
 | :----------------------------------------------| 
 | ["#####", "# # #", "### #", "# ##", "#####"]   |

#### 예시 설명  
- arr1
    - 9  -> 01001 
    - 20 -> 10100
    - 28 -> 11100
    - 18 -> 10010
    - 11 -> 01010
    
- arr2
    - 30 -> 11110
    - 1  -> 00001
    - 21 -> 10101
    - 17 -> 10001
    - 28 -> 11100
    
- 비트 or 연산 사용 
    - 9  | 30 = 11111 => #####
    - 20 | 1  = 10101 => # # #
    - 28 | 21 = 11101 => ### #
    - 18 | 17 = 10011 => #  ##
    - 11 | 28 = 11110 => #### 
    
### 코드 구조 구상
- n 길이만큼 반복 
- arr1[i]|arr2[i] = arrSum[i]
- 이진수 자릿수가 부족하면 채워주는 zfill 사용 
- if로 arrSum[i]의 요소가 1이면 '#', 아니면 '@'
- 공백은 join 하면 사라지므로 @로 해서 합치고 나서 공백으로 변환 
- append로 answer 배열에 추가    
   
### 사용한 함수 
- zfill(n)
- append
- zoin
- replace

### 코드 구현
  
<pre>
<code>
def solution(n, arr1, arr2):
    answer = []    
    
    for i in range(n):
        bit = 0
        numBit = 0
        bit = bin(arr1[i] | arr2[i])
        numBit = bit[2:]
        b = numBit.zfill(n)
        c = []
        for i in range(n):
            if b[i] == '1':
                c.append('#')
            else:
                c.append('@')
        d = ('').join(c)
        answer.append(d.replace('@',' '))

</code>
</pre>








## 문제 출처 
[프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3)


#참고 사이트 
