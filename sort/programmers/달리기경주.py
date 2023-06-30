def solution(players, callings):
    name = {i:p for i,p in enumerate(players)}
    idx = {p:i for i,p in enumerate(players)}
    
    for i in callings:
        curr = idx[i]
        prior = curr-1
        
        if curr==0:
            pass
        else:
            name_prior = name[prior]
            name[curr] = name_prior
            name[prior] = i
            
            idx[i] = prior
            idx[name_prior] = curr
            
        
    answer = list(name.values())
    return answer
