import sys

n, k = map(int, sys.stdin.readline().split())

grades = list(map(int, sys.stdin.readline().split()))

for _ in range(k):
    start, end = map(int, sys.stdin.readline().split())
    ranges = grades[start-1:end]
    sums = 0
    for i in ranges:
        sums +=i
    ans = str(round(sums/(end-start+1),2))
    if ans[-3]=='.':
        print(ans)
    else:
        print(ans+'0')
