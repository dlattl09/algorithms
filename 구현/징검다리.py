# 일차시도 : 테케에서 실패

import sys

n = sys.stdin.readline()

stones = list(map(int, sys.stdin.readline().split()))

n= int(n)

temp = [1]*n

for i in range(n):
    orig = stones[i]
    for j in range(i+1,n):
        if stones[j]>orig:
            temp[i] +=1
            orig = stones[j]
        else:
            continue
print(max(temp))
print(temp)
