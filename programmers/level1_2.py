def solution(lottos, win_nums):
    same = 0
    zero = lottos.count(0)
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    for i in lottos:
        if i in win_nums:
            same+=1
    return rank[same+zero],rank[same]