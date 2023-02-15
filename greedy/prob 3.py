# 프로그래머스/그리디
# 큰 수 만들기

import itertools

def solution(number, k):
  """
풀이 (1)
기존의 itertools 라이브러리를 사용해서 하는 풀이
하지만 이 경우 테스크 케이스에 대해서 시간초과가 난다.
"""
    number = list(number)
    k = len(number)-k
    comb = list(itertools.combinations(number,k))
    for i in range(len(comb)):
        comb[i] = ''.join(comb[i])
    comb = map(int, comb)
        
    answer = str(max(comb))
    return answer
  
  #######
  
  def solution(number, k):
    """
    풀이 (2)
    풀이 (1)과 비슷하며 최대한 for문을 없애주었지만, 여젆 시간초과 문제 발생 -> itertools 함수를 사용핮 않는 것ㅇ 나을 수도 있을듯
    """
    number = list(number)
    k = len(number)-k
    comb = list(map(''.join, itertools.combinations(number, k)))      
    answer = str(max(comb))
    return answer
  
  ########
  
  def solution(number, k):
    """
    풀이 (3)
    테스트 케이스에 대해서 limit이 굉장히 컸기 때문에 최대하 O(N)의 복잡도 이하로 푸는게 좋음 -> itertools로 조합의 경우르 고려하면 경우의 숙 많아질 ㅅ 있으므로 이거 사용 안하기로 함
    """
    number = list(number)
    answer = [number.pop(0)]
    
    for num in number:
        while k>0 and len(answer)!=0 and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
    while k>0:
        answer.pop()
        k-=1
       
    return ''.join(answer)
  
  
