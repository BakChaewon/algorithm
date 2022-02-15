def solution(s):
    #a=""
    #for i in sorted(s, reverse=True):
        #a += i
    #return a
    a=''.join(sorted(s, reverse=True))
    return a

#sorted는 리스트를 정렬. 문자열 정렬 가능하지만 리스트로 반환. 또한 대문자는 소문자보다카는것으로 판단.
#내림차순 정렬은 reverse를 true로 지정해주면 된다.
#join함수를 사용해서 매개변수로 들어온 리스트를 문자열로 합쳐준다. '구분자'.join(리스트)