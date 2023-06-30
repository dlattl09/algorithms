def solution(name, yearning, photo):
    yearn = {n:y for n,y in zip(name, yearning) }
    answer = []
    for i in photo:
        ans = 0
        for j in i:
            if j in name:
                ans+=yearn[j]
        answer.append(ans)
            
    return answer
