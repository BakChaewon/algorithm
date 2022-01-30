def solution(numbers):
    # for i in range(0,len(numbers)-1):
    #     for j in range(i+1,len(numbers)):
    #         answer.append(numbers[i]+numbers[j])
    # answer=sorted(set(answer))
    answer = [numbers[i]+numbers[j] for i in range(0, len(numbers)-1) for j in range(i+1, len(numbers))]
    return sorted(list(set(answer)))
