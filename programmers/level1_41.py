def solution(s):
    # answer = ""
    # lis = []
    # words = s.split()
    # for word in words:
    #     answer = ""
    #     for i in range(len(word)):
    #         if((i+1)%2!=0):
    #             answer+=word[i].upper()
    #         else:
    #             answer += word[i].lower()
    #     lis.append(answer)
    # return " ".join(lis)
    tmp = 1
    answer = []
    for i in s:
        if(i==" "):
            tmp = 1
            answer.append(" ")
            continue
        elif(tmp%2!=0):
            answer.append(i.upper())
        else:
            answer.append(i.lower())
        tmp+=1
    return "".join(answer)
    
# 한 줄로 쓰는 다른 방법이 있는듯. 보고싶진 않고 방법을 생각해내라!