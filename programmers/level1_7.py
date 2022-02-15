def solution(numbers):
    #     answer = 0
    #     all = [1,2,3,4,5,6,7,8,9,0]
    #     for i in numbers:
    #         del all[all.index(i)]
    #     for j in all:
    #         answer+=j
            
    #     for i in all:
    #         if i not in numbers:
    #             answer+=i

    return sum(i for i in range(1,10) if i not in numbers)