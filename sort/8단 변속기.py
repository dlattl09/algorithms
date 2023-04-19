import sys

inputs = list(map(int, sys.stdin.readline().split())) 

ascending = 1
descending = 1

start = inputs[0]
for i in inputs[1:]:
    if i==start+1:
        ascending +=1
    if i==start-1:
        descending +=1
    start = i

if ascending == 8:
    print("ascending")
if descending == 8:
    print("descending")
if ascending != 8 and descending !=8:
    print("mixed")
