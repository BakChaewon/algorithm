# 처음 작성했던 코드 / heapq를 몰랐고, 효율성 테스트를 통과하지 못했음
# def solution(scoville, K):
#     cnt = 0
#     scv = 0
#     while(1):
#         if(len(scoville)<=1):
#             return -1
#         scoville.sort()
#         a = scoville.pop(0)
#         b = scoville.pop(0)
#         scv = a + b*2
#         scoville.append(scv)
#         cnt+=1
#         for i in scoville:
#             if(i<K):
#                 break
#         else:
#             return cnt


# 질문을 둘러보니 heapq라는 라이브러리를 사용해야하는 듯 싶어 기존 코드에서 일부만을 수정했다.
# 효율성 테스트 통과!
# scoville 리스트 내에 값들이 K보다 큰지 확인하는 for문에서 인덱스로 접근했는데 현재의 방법이 더 좋은 효율성 결과를 냄.
# 왜냐면 heapq의 0번째 인덱스의 값이 가장 작은 값이라고 해서 1번째 인덱스의 값이 두번째로 작은 값이 아니기 때문이다.
# 추가적으로, 초기화가 필요한 변수가 아니면 미리 정의해둘 필요 없음. 수식을 한군데에서만 사용한다면 변수 지정할 필요 없이 바로 넣어주면 된다. (근데 이게 좋은 방법인지는 모르겠다.)
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while(1):
        if(len(scoville)<=1):
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        cnt+=1
        for i in scoville:
            if(i<K):
                break
        else:
            return cnt