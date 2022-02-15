def solution(n):
    tmp=[]
    while(n>=1):
        tmp.append(n%3)
        n=n//3
    tmp.reverse()
    return sum(tmp[i]*(3**i) for i in range(len(tmp)))