def solution(record):
    dic = {}
    answer = []
    for i in range(len(record)-1,-1,-1):
        record[i] = record[i].split()
        if(record[i][0]!="Leave" and record[i][1] not in dic.keys()):
            dic[record[i][1]] = record[i][2]
    for s in record:
        if(s[0] == "Enter"):
            answer.append("{0}님이 들어왔습니다.".format(dic[s[1]]))
        elif(s[0] == "Leave"):
            answer.append("{0}님이 나갔습니다.".format(dic[s[1]]))
    return answer

# split 한 리스트를 기존 리스트에 저장하지 않는 코드. 더 효율성이 좋다. 이차원 배열에 인덱싱으로 접근하는게 오래 걸리는건가?
# def solution(record):
#     dic = {}
#     answer = []
#     for i in record[::-1]:
#         tmp = i.split()
#         if(tmp[0]!="Leave" and tmp[1] not in dic.keys()):
#             dic[tmp[1]] = tmp[2]
#     for s in record:
#         tmp = s.split()
#         if(tmp[0] == "Enter"):
#             answer.append("{0}님이 들어왔습니다.".format(dic[tmp[1]]))
#         elif(tmp[0] == "Leave"):
#             answer.append("{0}님이 나갔습니다.".format(dic[tmp[1]]))
#     return answer