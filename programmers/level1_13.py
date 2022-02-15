# 내 풀이
def solution(answers):
    students = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    counter = [0,0,0]
    
    # 정답 크기만큼 찍은 번호 리스트 만들어주기 
    for i,a in enumerate(students):
        students[i] = a*(len(answers)//len(a))+a[:len(answers)%len(a)]    
        
    # 맞춘 갯수 완전 탐색
    for i, students in enumerate (students):
        tmp = [n for n,m in zip(students, answers) if n==m]
        counter[i] = len(tmp)

    # 많이 맞춘 사람
    mx = max(counter)
    return [i+1 for i,c in enumerate(counter) if c==mx]

# 다른 사람 풀이는 문제 갯수만큼 리스트를 늘려주지 않고 나머지 연산을 통해 계산!

# 다른 사람의 풀이 참고해서 푼 것
# def solution(answers):
#     students = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
#     counter = [0,0,0]
    
#     for i, n in enumerate(answers):
#         if(students[0][i%len(students[0])]==n):
#             counter[0]+=1
#         if(students[1][i%len(students[1])]==n):
#             counter[1]+=1
#         if(students[2][i%len(students[2])]==n):
#             counter[2]+=1
#     return [i+1 for i,c in enumerate(counter) if c==max(counter)]