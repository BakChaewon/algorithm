# 에라토스테네스의 체 사용한 풀이

# def solution(n):
#     a = [False,False] + [True]*(n-1) #0과 1을 제외한 모든 수를 소수라 True로 정의해놓고
#     primes=[]

#     for i in range(2,n+1): # 2부터 n까지 모든 수를 돌면서
#         if a[i]: # 해당 인덱스가 True면 
#             primes.append(i) # 소수 리스트에 추가하고
#             for j in range(2*i, n+1, i): # 배수를 모두 False로 만든다.
#                 a[j] = False
#     return len(primes) # 최종적으로 소수 리스트의 사이즈 반환

# 원래 이거 통과 안됐었는데 바뀐듯. 효율성 테스트 통과함.
def solution(n):
    prime = []
    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
        # for j in prime:
        #     if(j>int(i**0.5)+1):
        #         prime.append(i)
        #         break
            if(i%j == 0):
                break
        else:
            prime.append(i)
    return len(prime)