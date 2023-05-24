# 시간제한 초과 
import sys
 
n = int(sys.stdin.readline())

results = []
for _ in range(3):
    results.append(list(map(int, sys.stdin.readline().split())))

total = []
rank1 = [1]*n
rank2 = [1]*n
rank3 = [1]*n
totalrank = [1]*n
for i in range(n):
    total.append(results[0][i]+results[1][i]+results[2][i])

for i in range(n):
    for j in range(n):
        if results[0][i] < results[0][j]:
            rank1[i]+=1
        if results[1][i] < results[1][j]:
            rank2[i]+=1
        if results[2][i] < results[2][j]:
            rank3[i]+=1
        if total[i] < total[j]:
            totalrank[i]+=1


print(*rank1)
print(*rank2)
print(*rank3)
print(*totalrank)

