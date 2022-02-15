def solution(dartResult):
    answer = []
    tmp=0
    for i,d in enumerate(dartResult):
        if(d.isdigit()):
            if(tmp==10 and d=="0" and dartResult[i-1]=="1"):
                continue
            answer.append(tmp)
            tmp=int(d)
            if(d+dartResult[i+1]=="10"):
                tmp = 10
        elif(d.isalpha()):
            if(d=="D"):
                tmp=tmp**2
            elif(d=="T"):
                tmp=tmp**3
            else:
                tmp = tmp**1
        else:
            if(d=="#"):
                tmp*=-1
            elif(d=="*"):
                tmp*=2
                answer[-1]*=2
    answer.append(tmp)
    print(answer)
    return sum(answer)