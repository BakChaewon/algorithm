def solution(n):
    # if(int(n**0.5) == n**0.5):
    #     return (n**0.5+1)**2
    # else:
    #     return -1
    return (int(n**0.5) == n**0.5) and (n**0.5+1)**2 or -1

# and 와 or을 사용해서 푼것 (다른 사람의 풀이)
# not > and > or 우선순위
# 1과 n(값)을 and하면 n 값이 결과로 나온다.