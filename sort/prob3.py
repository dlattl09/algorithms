# k번째 수

def solution(citations):
  """
  이거 풀이 오 테케에 대해서느 안되는지 모르겠음
  -> 아 논문 수라 인용 수랑 헷갈리지 말기!
  """
    citations.sort()
    answer = 0
    for num, i in enumerate(citations):
        val1 = len(citations[num:]) #이상
        val2 = len(citations[:num+1]) #이하
        if val1 >=i and val2<=i and answer<i:
            answer = i
            break
            
    return answer
  
  ==================
  
  
  def solution(citations):
    """
    통과된 풀이
    """
    citations.sort()
    answer = 0
    for num, i in enumerate(citations):
        if i>=len(citations)-num:
            answer = len(citations)-num
            break
            
    return answer
  
  
