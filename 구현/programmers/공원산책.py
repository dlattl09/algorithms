def solution(park, routes):
    
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    directions = {'E':0,'S':3,'W':1,'N':2}
    n_col = len(park[0])
    n_row = len(park)
    for i in range(n_row):
        for j in range(n_col):
            if park[i][j] == "S":
                nx = i
                ny = j
    
    for route in routes:
        direct = directions[route[0]]
        amount = route[-1]
        flag = 0
        x = nx
        y = ny
        for _ in range(int(amount)):
            x += dx[direct]
            y += dy[direct]
            if x>=n_row or y>=n_col or x<0 or y<0 or park[x][y]=='X':
                flag +=1
                break
        if flag ==0:
            nx +=  dx[direct]*int(amount)
            ny += dy[direct]*int(amount)  

    answer = [nx,ny]
    return answer
