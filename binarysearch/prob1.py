import copy
def solution(n, times):
  """
  테케에 대해서 시간초과 남 -> 아마 min 함수으 사용같음
  """
    answer = 0
    times.sort()
    done = 0
    update = copy.deepcopy(times)
    while done<n:
        val = int(min(update))
        ind = int(update.index(val))
        update[ind] += times[ind]
        done +=1
            
        
    return val
