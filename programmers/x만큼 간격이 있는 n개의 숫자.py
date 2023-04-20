def solution(x, n):
    # 1
    # tmp = 1 if x>=0 else -1
    # #다양한 입력을 고려해줘야 한다는 점
    # if x==0: # 아래 range에서 x가 0이 되면 런타임 에러 -> range(0,1,0) -> 그렇기 때문에 x가 0인 경우를 고려해줘야함
    #     return [0]*n
    # else:
    #     return list(range(x,x*n+tmp,x))
    
    # 2
    # 그냥 더해주는 방법
    return [x*i for i in range(1,n+1)]
