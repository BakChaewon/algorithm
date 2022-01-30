def solution(sizes):
    max_i = 0
    max_j = 0
    for a,b in sizes:
        if(a<b):
            a, b = b, a
        max_i = max(max_i, a)
        max_j = max(max_j, b)
    return max_i*max_j