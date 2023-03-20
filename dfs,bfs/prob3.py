# 게임 맵 최단거리 (프로그래머스)
# level 2

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx <0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))
        
    answer = maps[n-1][m-1]
    if answer ==1:
        answer = -1
    return answer
