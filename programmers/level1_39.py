import string
def solution(s, n):
    answer = ""
    for i in s:
        if(i==" "):
            answer += " "
        else:
            if(i.islower()):
                answer += string.ascii_lowercase[(string.ascii_lowercase.index(i)+n)%len(string.ascii_lowercase)]
            else:
                answer += string.ascii_uppercase[(string.ascii_uppercase.index(i)+n)%len(string.ascii_uppercase)]
    return answer