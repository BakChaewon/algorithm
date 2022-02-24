def solution(s):
    stack =[]
    for i in s:
        if(stack == [] or stack[-1]!=i):
            stack.append(i)
        else:
            stack.pop()
    if(stack == []):
        return 1
    else:
        return 0