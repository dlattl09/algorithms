import sys
from collections import defaultdict

inputs = list(map(int, sys.stdin.readline().split())) 
names = []
for i in range(inputs[0]):
    names.append(sys.stdin.readline().split()[0])

rooms = defaultdict(list)#.fromkeys(names, list)
#for i in rooms.keys():
 #   rooms[i] = [[9,9]]
for i in range(inputs[1]):
    inform = list(map(str, sys.stdin.readline().split())) 
    
    rooms[inform[0]].append([int(inform[1]), int(inform[2])])
 
if len(rooms)!=len(names):
    temp3 = list(set(names) - set(rooms.keys()))
    for i in temp3:
        rooms[i] = [[9,9]]

rooms = sorted(rooms.items())

for i in range (len(rooms)):
    times = rooms[i][1]
    times.append([18,18])
    times.sort()
    start = 9
    available = []
    if i>0:
        print('-----')
    for j in times:
        avail = j[0]-start
        if avail>0:
            available.append([start, j[0]])
        start = j[1]
    print("Room", str(rooms[i][0])+':')
    if len(available)==0:
        print("Not available")
    else:
        print(len(available), "available:")
        for k in available:
            if k[0]==9:
                k[0]='09'
            print(str(k[0])+'-'+str(k[1]))


