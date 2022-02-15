def solution(n):
    # answer=[]
    # tmp=0
    # for i in range(2,n+1):
    #     for j in answer:
    #         if(j>=n**0.5):
    #             answer.append(i)
    #             break
    #         if(i%j==0):
    #             break
    #     else:
    #         answer.append(i)
    # return len(answer)
    
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return len(primes)