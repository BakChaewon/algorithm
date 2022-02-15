def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)

#문제를 잘 읽자
#isnumeric, isdigit, isdecimal 함수가 존재하는데 뉴머릭은 숫자값 표현에 해당하는 글자까지 포함, 디짓은 숫자로 보이는 모든 글자 포함, 데시말은 int형으로 변형 가능한지