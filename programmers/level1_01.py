# def solution(id_list, report, k):
#     mail = [0]*len(id_list)
#     count = [[0] for i in range(len(id_list))]
#     for rep in report:
#         p = rep.split(' ')[0]
#         q = rep.split(' ')[1]
#         count[id_list.index(q)].append(id_list.index(p))
#     for i in range(len(count)):
#         del count[i][0]
#         count[i] = set(count[i])
#         if(len(count[i])>=k):
#             for j in count[i]:
#                 mail[j] +=1
#     return mail

# list의 index를 사용하지 않고, dic을 만들어서 실행 시간 줄이기.
def solution(id_list, report, k):
    mail = [0]*len(id_list)
    count = [[0] for i in range(len(id_list))]
    dic = {}
    for i in range(len(id_list)):
        dic[id_list[i]] = i
    for rep in report:
        p = rep.split(' ')[0]
        q = rep.split(' ')[1]
        count[dic[q]].append(dic[p])
    for i in range(len(count)):
        del count[i][0]
        count[i] = set(count[i])
        if(len(count[i])>=k):
            for j in count[i]:
                mail[j] +=1
    return mail