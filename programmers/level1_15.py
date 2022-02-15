def solution(nums):
    # 폰켓몬중 중복을 제거한 폰켓몬 갯수가 가져갈 수 있는 갯수보다 많으면 중복되지 않고 가져갈 수 있고,
    # 중복 제거한 폰켓몬 갯수가 가져갈 수 있는 폰켓몬 갯수보다 적으면 가져갈 수 있는 종류 갯수는 중복되지 않는 폰켓몬 갯수이다.
    # 그니까! 중복 제거한 갯수만큼 가져갈 수 있는데 내가 가져갈 수 있는 폰켓몬 갯수가 n/2개니까 min을 통해서 구할 수 있다.
    
    # if(len(set(nums))>=len(nums)//2):
    #     return len(nums)//2
    # else:
    #     return len(set(nums))
    
    # return len(set(nums)) if (len(set(nums))<len(nums)//2) else len(nums)//2
    
    return min(len(set(nums)), len(nums)//2)