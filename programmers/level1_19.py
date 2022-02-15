def solution(d, budget):
    d.sort()
    sum=0
    answer=0
    for i in d:
        sum+=i
        if(sum>budget):
            break
        answer+=1
    return answer