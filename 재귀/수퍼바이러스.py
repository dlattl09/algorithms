import sys

def virus(p,n):
    if n ==1:
        return p
    elif n%2 ==0:
        ans = virus(p, n//2)
        ans = (ans*ans)%1000000007
        return ans
    else:
        ans = virus(p, n//2)
        ans = (ans*ans*p)%1000000007
        return ans


k, p, n = map(int, sys.stdin.readline().split())
n = n*10
ans = virus(p,n)
print((ans*k)%1000000007)
