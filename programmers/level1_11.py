def solution(participant, completion):
    # dic = {}
    # for i in completion:
    #     dic[i] = dic.get(i, 0)+1
    # for j in participant:
    #     if(participant.count(j)!=dic.get(j,0)):
    #         return j
    
    dic = {}
    for i in completion:
        dic[i] = dic.get(i,0)+1
    for i in participant:
        # if(dic.get(i,0) != participant.count(i)):
        #     return i
        dic[i] = dic.get(i,0)-1
        if(dic[i] < 0):
            return i
        
# 정렬해서 값을 차례대로 비교하는 방법도 있고, counter 객체를 사용해서 뺄셈 연산을 하는 방법도 있다.