def solution(absolutes, signs):
    # return sum(i if p else -i for i, p in zip(absolutes, signs))
    # answer = 0
    # for i, s in zip(absolutes, signs):
    #     if s:
    #         answer += i
    #     else:
    #         answer -= i
    # return answer
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i] 
        else:
            answer -= absolutes[i] 
    return answer