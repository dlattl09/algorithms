# 프로그래머스 등굣길

def solution(m, n, puddles):
  """
  테케에 대해서 70점 나옴.. 뭐가 문제지
  """
    d = [[1] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i==1 or j==1:
                continue
            elif [i,j] in puddles:
                d[i][j] = 0
            else:
                d[i][j] = (d[i - 1][j] + d[i][j - 1])%1000000007
    return d[m][n]
