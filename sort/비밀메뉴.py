import sys

inputs = list(map(int, sys.stdin.readline().split())) 
m = "".join(list(map(str, sys.stdin.readline().split())))
n = "".join(list(map(str, sys.stdin.readline().split())))


if m in n:
    print('secret')
else:
    print('normal')
