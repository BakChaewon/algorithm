def solution(x):
    # s = 0
    # for i in str(x):
    #     s += int(i)
    # return x%s==0
    return x%sum([int(i) for i in str(x)]) == 0

# for문을 돌아서 합을 구하는 코드는 list와 sum을 사용해서 한 줄로 줄일 수 있다.