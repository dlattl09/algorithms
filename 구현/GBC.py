import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
rule = deque()
ans = []

for i in range(n):
    rule.append(list(map(int, sys.stdin.readline().split())))
for i in range(m):
    test=list(map(int, sys.stdin.readline().split()))
    while test[0]!=0:
        if rule[0][1] <= test[1]:
            ans.append(test[1]-rule[0][1])
        else:
            ans.append(0)
        if rule[0][0] <= test[0]:
            test[0] = test[0]-rule[0][0]
            rule.popleft()
        else:
            rule[0][0] = rule[0][0]-test[0]
            test[0] = 0
        

print(max(ans))
