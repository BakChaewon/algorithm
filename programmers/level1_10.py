from itertools import combinations

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

def solution(nums):
    answer = 0
    lis = list(combinations(nums, 3))
    for num in lis:
        if (isPrime(sum(num))):
            answer+=1
    return answer