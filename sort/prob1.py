#k번째 수

def solution(array, commands):
    answer = []
    for com in commands:
        i,j,k = com
        ans = array[i-1:j]
        ans.sort()
        answer.append(ans[k-1])
    return answer
