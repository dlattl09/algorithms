# 체육복
# level 1

def solution(n, lost, reserve):
    lost_diff = list(set(lost)-set(reserve))
    lost_diff.sort()
    reserve_diff = list(set(reserve)-set(lost))
    reserve_diff.sort()
    for i in reserve_diff:
        for j in lost_diff:
            if j==i+1:
                lost_diff.remove(j)
            elif j==i-1:
                lost_diff.remove(j)
    answer = n-len(lost_diff)
    return answer
