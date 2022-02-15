def solution(N, stages):
    dic = {}
    whole = len(stages)
    for i in range(1,N+1):
        if (whole!=0):
            count = stages.count(i)
            dic[i]=count/whole
            whole = whole-count
        else:
            dic[i]=0
    return list(sorted(dic, key=lambda x:dic[x], reverse=True))