# 정수삼각형

def solution(triangle):
    triangle.reverse()

    for num, i in enumerate(triangle):
        for j in range (len(i)):
            if num>0:
                triangle[num][j] += max(triangle[num-1][j],triangle[num-1][j+1])           
    return i[-1]
