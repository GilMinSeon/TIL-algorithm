import math

def solution(progresses, speeds):
    answer = []
    
    date_list = []
    for i in range(len(progresses)):
        progress, speed = progresses[i], speeds[i]
        date = (100-progress)/speed
        date_list.append(math.ceil(date))
      
    max_val = date_list[0]
    res = 1
    
    for i in range(1, len(date_list)):
        target = date_list[i]
        
        if max_val < target:
            answer.append(res)
            max_val = target
            res = 1
        else:
            res += 1
            
        if i == len(date_list)-1 :
            answer.append(res)
    
    return answer