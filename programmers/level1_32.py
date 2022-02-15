def solution(s):
    return (s.count('p')+s.count('P'))==(s.count('y')+s.count('Y'))
#대문자, 소문자 각각의 갯수를 세지 않고, lower한 후에 카운트 하는 방법도 존재