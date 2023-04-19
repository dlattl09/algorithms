import sys


w, n = map(int, sys.stdin.readline().split())
 
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

jewels.sort(key=lambda x: x[1], reverse=True)
price = 0
for i in jewels:
    if w > i[0]:
        w -= i[0]
        price += i[0]*i[1]
    else:
        price += w*i[1]
        break
print(price)
