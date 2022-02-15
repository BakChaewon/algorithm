def solution(num):
    tmp = 0
    while(num!=1):
        if(num%2==0):
            num = num/2
        else:
            num = num*3 + 1
        tmp+=1
        if(tmp>500):
            return -1
    return tmp