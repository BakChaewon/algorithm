def solution(n):
    #return "".join([int(i) for i in str(n)][::-1])
    #answer = sorted([int(i) for i in str(n)], reverse=True)
    #return answer
    return int("".join(sorted(str(n), reverse=True)))

# sorted는 리스트를 리턴