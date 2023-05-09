import sys
from collections import deque

h,w = map(int, sys.stdin.readline().split())
pixels = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
q = int(sys.stdin.readline())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,c):
    queue = deque()
    queue.append((x,y))
    color = pixels[x][y]
    pixels[x][y] = c
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=0 and nx<h and ny>=0 and ny<h:
                if pixels[nx][ny]==color:
                    pixels[nx][ny] = c
                    queue.append((nx,ny))
                else:
                    continue




for _ in range(q):
    i,j,c = map(int, sys.stdin.readline().split())
    bfs(i-1,j-1,c)

for i in range(h):
    for j in range(w):
        print(pixels[i][j], end=" ")
    print()
