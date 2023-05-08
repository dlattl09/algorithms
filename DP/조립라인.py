import sys

n = sys.stdin.readline()
n = int(n)

temp = []
for _ in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))

da =[0]*n
db = [0]*n

da[0] = temp[0][0]
db[0] = temp[0][1]


for i in range(1,n):
    da[i] = temp[i][0] + min(da[i-1], db[i-1]+temp[i-1][3])
    db[i] = temp[i][1] + min(db[i-1], da[i-1]+temp[i-1][2])

print(min(da[n-1],db[n-1]))
