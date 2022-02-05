def solution(s):
    # 처음에 푼 것
    result = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for j in s:
        if(j.isnumeric()):
            result+=j
        else:
            tmp+=j
            if tmp in arr:
                result+=str(arr.index(tmp))
                tmp=""
    return int(result)

    #조금 나중에 푼 것
    # arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # for i in range (len(arr)):
    #     s = s.replace(arr[i], str(i))
    # return int(s)
    
    #enumerate 사용해서 푼 것.
    # arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # for i,c in enumerate(arr):
    #     s = s.replace(c,str(i))
    # return int(s)