import sys
N = int(sys.stdin.readline())
dn = [0]*16
dn[0] = 2

for i in range(1,N+1):
    dn[i] = dn[i-1] + (dn[i-1]-1)


print(dn[N]**2) 
