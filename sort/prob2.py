# 가자 큰 수 

def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : str(x)*4)
    numbers.reverse()
    for i in numbers:
        answer += str(i)
    if set(numbers)=={0}:
        answer = '0'
    return answer
