def solution(n, m):
    answer = []
    for i in range(n, 0, -1):
        if(n%i == 0 and m%i == 0):
            answer.append(i)
            break
    for j in range(n, n*m+1):
        if(j%n == 0 and j%m == 0):
            answer.append(j)
            break
    return answer