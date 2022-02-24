def solution(progresses, speeds):
    stack = list(reversed(progresses))
    speed = list(reversed(speeds))
    answer = []
    while(stack != []):
        cnt = 0
        for i in range(len(stack)-1,-1,-1):
            stack[i]+=speed[i]
        for i in range(len(stack)-1,-1,-1):
            if(i==len(stack)-1): # 가장 top에 있고
                if(stack[i]>=100): # 100을 넘었으면
                    cnt+=1
                    stack.pop()
                else:
                    break
        answer.append(cnt)
    return [i for i in answer if(i!=0)]

# 다른 사람의 풀이 최상단
# 직접 일일이 더해서 얼마만에 끝나느지를 구하는게 아니라 100에서 progresse 값을 빼서 그 값을 speed로 나눈 몫을 이용
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]

# 위 코드의 아이디어를 가져와 내가 작성한 코드    
# import math
# def solution(progresses,speeds):
#     q = []
#     answer = []
#     for p,s in zip(progresses, speeds):
#         q.append(math.ceil((100-p)/s))
#     print(q)
#     i=0
#     cnt = 1
#     for j in range(1, len(q)):
#         if(q[i]>=q[j]):
#             cnt+=1
#         else:
#             answer.append(cnt)
#             cnt=1
#             i=j
#     answer.append(cnt)
#     return answer