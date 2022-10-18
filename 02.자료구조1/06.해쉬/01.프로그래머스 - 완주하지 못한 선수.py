def solution(participant, completion):

    d = dict()
    for i in participant:
        d[i] = d.get(i,0) + 1
    for i in completion:
        d[i] = d.get(i,0) - 1
    
    for key,val in d.items():
        if val > 0:
            return key
    
