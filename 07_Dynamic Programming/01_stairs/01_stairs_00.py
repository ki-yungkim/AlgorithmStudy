score = [0]
N = int(input())
for i in range(N):
    score.append(int(input()))

if N == 1:
    print(score[1])
else:
    score_total = [0] * (N+1)
    score_total[1] = score[1]
    score_total[2] = score[1] + score[2]

    for i in range(3, N+1):
        score_total[i] = max(score[i] + score[i-1] + score_total[i-3], score[i] + score_total[i-2])
     
    print(score_total[N])