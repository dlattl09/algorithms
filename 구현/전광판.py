import sys

numn = [0,0,0,0,0,0,0]
num0 = [1,1,1,1,0,1,1]
num1 = [0,0,1,0,0,1,0]
num2 = [0,1,1,1,1,0,1]
num3 = [0,1,1,0,1,1,1]
num4 = [1,0,1,0,1,1,0]
num5 = [1,1,0,0,1,1,1]
num6 = [1,1,0,1,1,1,1]
num7 = [1,1,1,0,0,1,0]
num8 = [1,1,1,1,1,1,1]
num9 = [1,1,1,0,1,1,1]

T = sys.stdin.readline()
for i in range(int(T)):
    inputs = list(map(str, sys.stdin.readline().split())) 
    A = list(inputs[0])
    B = list(inputs[1])
    switch = 0
    if len(A)<len(B):
        blank = list('n'*(len(B)-len(A)))
        a = blank + A
        b = B
    if len(B)<len(A):
        blank = list('n'*(len(A)-len(B)))
        b = blank + B
        a = A
    if len(A)==len(B):
        a = A
        b = B
    for i in range(len(a)):
        lista = globals()["num{}".format(a[i])]
        listb = globals()["num{}".format(b[i])]
        diff = [i for i, j in zip(lista, listb) if i != j]
        switch += len(diff)
    print(switch)




